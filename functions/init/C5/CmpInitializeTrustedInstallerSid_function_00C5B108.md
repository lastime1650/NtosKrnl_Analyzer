# CmpInitializeTrustedInstallerSid

- RVA: `0x00C5B108`–`0x00C5B186` (길이 `126` bytes)
- VA: `0x0000000140C5B108`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `28`개 명령, `126/126` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00C5B11F` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x00C5B131` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C5B150` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)

### Direct callers
- [CmInitSystem1](CmInitSystem1_function_00C559CC.md) at `0x00C55C40`

### Static image references
- `0x00C5B136` → RVA `0x00FD8070` (`PAGEDATA`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00C5B11F` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (`INIT` → `PAGE`)
  - `0x00C5B131` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C5B150` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C5B108  40 53                           push rbx
00C5B10A  48 83 EC 20                     sub rsp, 0x20
00C5B10E  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
00C5B113  B9 06 00 00 00                  mov ecx, 6
00C5B118  66 C7 44 24 34 00 05            mov word ptr [rsp + 0x34], 0x500
00C5B11F  E8 AC F3 D6 FF                  call 0x1409ca4d0
00C5B124  8B D0                           mov edx, eax
00C5B126  B9 00 01 00 00                  mov ecx, 0x100
00C5B12B  41 B8 43 6D 53 65               mov r8d, 0x65536d43
00C5B131  E8 BA 6F F2 FF                  call 0x140b820f0
00C5B136  48 89 05 33 CF 37 00            mov qword ptr [rip + 0x37cf33], rax
00C5B13D  48 8B D8                        mov rbx, rax
00C5B140  48 85 C0                        test rax, rax
00C5B143  74 3A                           je 0x140c5b17f
00C5B145  41 B0 06                        mov r8b, 6
00C5B148  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00C5B14D  48 8B C8                        mov rcx, rax
00C5B150  E8 CB 05 D9 FF                  call 0x1409eb720
00C5B155  C7 43 08 50 00 00 00            mov dword ptr [rbx + 8], 0x50
00C5B15C  C7 43 0C B5 89 FB 38            mov dword ptr [rbx + 0xc], 0x38fb89b5
00C5B163  C7 43 10 19 84 C2 CB            mov dword ptr [rbx + 0x10], 0xcbc28419
00C5B16A  C7 43 14 5C 6C 23 6D            mov dword ptr [rbx + 0x14], 0x6d236c5c
00C5B171  C7 43 18 57 00 77 6E            mov dword ptr [rbx + 0x18], 0x6e770057
00C5B178  C7 43 1C C0 02 64 87            mov dword ptr [rbx + 0x1c], 0x876402c0
00C5B17F  48 83 C4 20                     add rsp, 0x20
00C5B183  5B                              pop rbx
00C5B184  C3                              ret
00C5B185  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpInitializeTrustedInstallerSid(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_p8;
    unsigned __int16 v_stack_pC;

    v_rsp = (v_rsp) - (32);
    v_stack_pC = 0x500ULL;
    result = RtlLengthRequiredSid(6, a2, a3, a4);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)(0x65536D43ULL), a4);
    *(unsigned __int64 *)(v_rip + 3657523) = result;
    if (result != 0) {
        a3 = 6;
        a2 = v_stack_p8;
        a1 = result;
        result = RtlInitializeSid(a1, a2, a3, a4);
        *(unsigned int *)(result + 8) = 80;
        *(unsigned int *)(result + 12) = 0x38FB89B5ULL;
        *(unsigned int *)(result + 16) = 0xCBC28419ULL;
        *(unsigned int *)(result + 20) = 0x6D236C5CULL;
        *(unsigned int *)(result + 24) = 0x6E770057ULL;
        *(unsigned int *)(result + 28) = 0x876402C0ULL;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
void CmpInitializeTrustedInstallerSid(void)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_p8;
    uint16_t v_stack_pC;

    local_rsp = (local_rsp) - (32);
    v_stack_pC = 0x500ULL;
    result = RtlLengthRequiredSid(6, a2, a3, a4);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)(0x65536D43ULL), a4);
    *(uint64_t *)(v_rip + 0x37CF33) = result;
    if (result != 0) {
        a3 = 6;
        a2 = v_stack_p8;
        a1 = result;
        result = RtlInitializeSid(a1, a2, a3, a4);
        *(uint32_t *)(result + 0x8) = 80;
        *(uint32_t *)(result + 0xC) = 0x38FB89B5ULL;
        *(uint32_t *)(result + 0x10) = 0xCBC28419ULL;
        *(uint32_t *)(result + 0x14) = 0x6D236C5CULL;
        *(uint32_t *)(result + 0x18) = 0x6E770057ULL;
        *(uint32_t *)(result + 0x1C) = 0x876402C0ULL;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C5B108&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C5B108[BB_00C5B108]
  bb_00C5B145[BB_00C5B145]
  bb_00C5B17F[BB_00C5B17F]
  bb_00C5B185[BB_00C5B185]
  bb_00C5B108 -->|branch| bb_00C5B17F
  bb_00C5B108 -->|fallthrough| bb_00C5B145
  bb_00C5B145 -->|flow| bb_00C5B17F
```
