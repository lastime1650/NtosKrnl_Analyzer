# sub_009299A4

- RVA: `0x009299A4`–`0x009299F3` (길이 `79` bytes)
- VA: `0x00000001409299A4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008D940`
- 디코드: `21`개 명령, `79/79` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009299DA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009299DA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x009299AE` → [sub_009299F3](Unknown_function_009299F3.md) (`tail-transfer`)
  - `0x009299B9` → [sub_0092995A + 0xB](Unknown_function_0092995A.md) (`tail-transfer`)
  - `0x009299EE` → [sub_009298F8 + 0x12](Unknown_function_009298F8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009299A4  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
009299A8  48 03 C7                        add rax, rdi
009299AB  48 3B C8                        cmp rcx, rax
009299AE  73 43                           jae 0x1409299f3
009299B0  0F B7 41 02                     movzx eax, word ptr [rcx + 2]
009299B4  FF C2                           inc edx
009299B6  48 03 C8                        add rcx, rax
009299B9  EB AA                           jmp 0x140929965
009299BB  66 89 51 02                     mov word ptr [rcx + 2], dx
009299BF  48 8B D3                        mov rdx, rbx
009299C2  66 44 89 31                     mov word ptr [rcx], r14w
009299C6  89 71 04                        mov dword ptr [rcx + 4], esi
009299C9  48 83 C1 08                     add rcx, 8
009299CD  44 0F B6 43 01                  movzx r8d, byte ptr [rbx + 1]
009299D2  4E 8D 04 85 08 00 00 00         lea r8, [r8*4 + 8]
009299DA  E8 61 CE D9 FF                  call 0x1406c6840
009299DF  66 FF 47 04                     inc word ptr [rdi + 4]
009299E3  41 8B C6                        mov eax, r14d
009299E6  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
009299EB  40 88 2F                        mov byte ptr [rdi], bpl
009299EE  E9 17 FF FF FF                  jmp 0x14092990a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_009299A4(__int64 a1, int a2)
{
    __int64 result;
    unsigned __int64 v_stack_p38;

    result = (*(unsigned __int16 *)(v_rdi + 2)) + (v_rdi);
    a2 = (unsigned int)((a2) + 1);
    a1 = (a1) + (*(unsigned __int16 *)(a1 + 2));
}
```

## 5. (Beta) C Style

```c
int64_t sub_009299A4(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    uint64_t v_stack_p38;

    result = (*(uint16_t *)(local_rdi + 0x2)) + (local_rdi);
    Arg2 = (uint32_t)((Arg2) + 1);
    Arg1 = (Arg1) + (*(uint16_t *)(Arg1 + 0x2));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009299A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009299A4[BB_009299A4]
  bb_009299B0[BB_009299B0]
  bb_009299BB[BB_009299BB]
  bb_009299A4 -->|fallthrough| bb_009299B0
```
