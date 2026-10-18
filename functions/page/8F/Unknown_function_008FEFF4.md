# sub_008FEFF4

- RVA: `0x008FEFF4`–`0x008FF052` (길이 `94` bytes)
- VA: `0x00000001408FEFF4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00088304`
- 디코드: `22`개 명령, `94/94` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x008FF034` → [PiDmObjectGetCachedCmProperty + 0x57](PiDmObjectGetCachedCmProperty_function_008FEE70.md) (`tail-transfer`)
  - `0x008FF03C` → [PiDmObjectGetCachedCmProperty + 0x4C](PiDmObjectGetCachedCmProperty_function_008FEE70.md) (`tail-transfer`)
  - `0x008FF04D` → [PiDmObjectGetCachedCmProperty + 0x57](PiDmObjectGetCachedCmProperty_function_008FEE70.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008FEFF4  8B 45 E8                        mov eax, dword ptr [rbp - 0x18]
008FEFF7  0F 28 45 A0                     movaps xmm0, xmmword ptr [rbp - 0x60]
008FEFFB  0F 28 4D B0                     movaps xmm1, xmmword ptr [rbp - 0x50]
008FEFFF  41 C7 07 4E 00 00 00            mov dword ptr [r15], 0x4e
008FF006  0F 11 03                        movups xmmword ptr [rbx], xmm0
008FF009  0F 28 45 C0                     movaps xmm0, xmmword ptr [rbp - 0x40]
008FF00D  0F 11 4B 10                     movups xmmword ptr [rbx + 0x10], xmm1
008FF011  0F 28 4D D0                     movaps xmm1, xmmword ptr [rbp - 0x30]
008FF015  0F 11 43 20                     movups xmmword ptr [rbx + 0x20], xmm0
008FF019  F2 0F 10 45 E0                  movsd xmm0, qword ptr [rbp - 0x20]
008FF01E  0F 11 4B 30                     movups xmmword ptr [rbx + 0x30], xmm1
008FF022  F2 0F 11 43 40                  movsd qword ptr [rbx + 0x40], xmm0
008FF027  89 43 48                        mov dword ptr [rbx + 0x48], eax
008FF02A  0F B7 45 EC                     movzx eax, word ptr [rbp - 0x14]
008FF02E  66 89 43 4C                     mov word ptr [rbx + 0x4c], ax
008FF032  8B C1                           mov eax, ecx
008FF034  E9 8E FE FF FF                  jmp 0x1408feec7
008FF039  41 89 07                        mov dword ptr [r15], eax
008FF03C  E9 7B FE FF FF                  jmp 0x1408feebc
008FF041  41 C7 07 4E 00 00 00            mov dword ptr [r15], 0x4e
008FF048  B8 23 00 00 C0                  mov eax, 0xc0000023
008FF04D  E9 75 FE FF FF                  jmp 0x1408feec7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008FEFF4(int a1)
{
    *(unsigned int *)(v_r15) = 78;
    *(unsigned __int64 *)(v_rbx) = v_xmm0;
    *(unsigned __int64 *)(v_rbx + 16) = v_xmm1;
    *(unsigned __int64 *)(v_rbx + 32) = v_xmm0;
    *(unsigned __int64 *)(v_rbx + 48) = v_xmm1;
    *(unsigned __int64 *)(v_rbx + 64) = v_xmm0;
    *(unsigned int *)(v_rbx + 72) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 24)));
    *(unsigned __int16 *)(v_rbx + 76) = (unsigned __int16)(*(unsigned __int16 *)(v_rbp - 20));
}
```

## 5. (Beta) C Style

```c
int64_t sub_008FEFF4(int32_t Arg1)
{
    *(uint32_t *)(local_r15) = 78;
    *(uint64_t *)(local_rbx) = v_xmm0;
    *(uint64_t *)(local_rbx + 0x10) = v_xmm1;
    *(uint64_t *)(local_rbx + 0x20) = v_xmm0;
    *(uint64_t *)(local_rbx + 0x30) = v_xmm1;
    *(uint64_t *)(local_rbx + 0x40) = v_xmm0;
    *(uint32_t *)(local_rbx + 0x48) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x18)));
    *(uint16_t *)(local_rbx + 0x4C) = (uint16_t)(*(uint16_t *)(local_rbp - 0x14));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008FEFF4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008FEFF4[BB_008FEFF4]
  bb_008FF039[BB_008FF039]
  bb_008FF041[BB_008FF041]
```
