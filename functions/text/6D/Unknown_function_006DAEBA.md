# sub_006DAEBA

- RVA: `0x006DAEBA`–`0x006DAF1F` (길이 `101` bytes)
- VA: `0x00000001406DAEBA`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068A4C`
- 디코드: `25`개 명령, `101/101` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006DAEC6` → [MiLocatePagefileSubsection](../36/MiLocatePagefileSubsection_function_00367AC0.md) (function, `0x00367AC0`)
- `0x006DAF11` → [MiComputeContiguousSubsectionPte](../44/MiComputeContiguousSubsectionPte_function_00444E10.md) (function, `0x00444E10`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006DAF1A` → [MiAdvanceVadView + 0x34](../2A/MiAdvanceVadView_function_002A60EC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DAEBA  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
006DAEC1  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
006DAEC6  E8 F5 CB C8 FF                  call 0x140367ac0
006DAECB  8B 48 20                        mov ecx, dword ptr [rax + 0x20]
006DAECE  4C 8B C8                        mov r9, rax
006DAED1  8B 40 24                        mov eax, dword ptr [rax + 0x24]
006DAED4  81 E1 C0 FF 00 00               and ecx, 0xffc0
006DAEDA  44 0F B6 47 21                  movzx r8d, byte ptr [rdi + 0x21]
006DAEDF  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
006DAEE4  48 C1 E1 1A                     shl rcx, 0x1a
006DAEE8  48 0B C8                        or rcx, rax
006DAEEB  49 C1 E0 20                     shl r8, 0x20
006DAEEF  8B 47 1C                        mov eax, dword ptr [rdi + 0x1c]
006DAEF2  48 2B D1                        sub rdx, rcx
006DAEF5  4C 0B C0                        or r8, rax
006DAEF8  4C 89 4F 48                     mov qword ptr [rdi + 0x48], r9
006DAEFC  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
006DAF00  48 8D 0C D0                     lea rcx, [rax + rdx*8]
006DAF04  48 2B D3                        sub rdx, rbx
006DAF07  48 89 4F 50                     mov qword ptr [rdi + 0x50], rcx
006DAF0B  49 03 D0                        add rdx, r8
006DAF0E  49 8B C9                        mov rcx, r9
006DAF11  E8 FA 9E D6 FF                  call 0x140444e10
006DAF16  48 89 47 58                     mov qword ptr [rdi + 0x58], rax
006DAF1A  E9 01 B2 BC FF                  jmp 0x1402a6120
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006DAEBA(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;

    result = MiLocatePagefileSubsection(v_rbp + 128, a6, a3, a4);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32))) & (0xFFC0ULL));
    a1 = (a1) << (26);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(result + 36)));
    a3 = (*(unsigned __int8 *)(v_rdi + 33)) << (32);
    a2 = (a6) - (a1);
    a3 = (a3) | ((unsigned int)(*(unsigned int *)(v_rdi + 28)));
    *(unsigned __int64 *)(v_rdi + 72) = result;
    a2 = (a2) - (v_rbx);
    *(unsigned __int64 *)(v_rdi + 80) = *(unsigned __int64 *)(result + 8) + a2 * 8;
    a2 = (a2) + (a3);
    result = MiComputeContiguousSubsectionPte(result, a2, a3, result);
    *(unsigned __int64 *)(v_rdi + 88) = result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_006DAEBA(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6)
{
    int64_t result;

    result = MiLocatePagefileSubsection(local_rbp + 128, Arg6, Arg3, Arg4);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20))) & (0xFFC0ULL));
    Arg1 = (Arg1) << (26);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(result + 0x24)));
    Arg3 = (*(uint8_t *)(local_rdi + 0x21)) << (32);
    Arg2 = (Arg6) - (Arg1);
    Arg3 = (Arg3) | ((uint32_t)(*(uint32_t *)(local_rdi + 0x1C)));
    *(uint64_t *)(local_rdi + 0x48) = result;
    Arg2 = (Arg2) - (local_rbx);
    *(uint64_t *)(local_rdi + 0x50) = *(uint64_t *)(result + 0x8) + Arg2 * 8;
    Arg2 = (Arg2) + (Arg3);
    result = MiComputeContiguousSubsectionPte(result, Arg2, Arg3, result);
    *(uint64_t *)(local_rdi + 0x58) = result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DAEBA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006DAEBA[BB_006DAEBA]
```
