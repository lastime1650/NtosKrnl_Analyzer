# FsRtlpAllocateOplock

- RVA: `0x009F1C74`–`0x009F1D5E` (길이 `234` bytes)
- VA: `0x00000001409F1C74`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A5F4C`
- 디코드: `56`개 명령, `234/234` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009F1C8E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009F1CA9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009F1CCF` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x009F1D16` → [Feature_3609177402__private_IsEnabledDeviceUsageNoInline](../../text/58/Feature_3609177402__private_IsEnabledDeviceUsageNoInline_function_00581D30.md) (function, `0x00581D30`)
- `0x009F1D2D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [FsRtlpOplockStoreKeyForDeleteOperation](../../text/3F/FsRtlpOplockStoreKeyForDeleteOperation_function_003F2A90.md) at `0x003F2B6E`
- [FsRtlpRequestExclusiveOplock](../../text/3F/FsRtlpRequestExclusiveOplock_function_003F3800.md) at `0x003F384F`
- [FsRtlpRequestShareableOplock](../../text/4E/FsRtlpRequestShareableOplock_function_004E6EC8.md) at `0x004E6F3B`
- [FsRtlpOplockFsctrlInternal](FsRtlpOplockFsctrlInternal_function_009F1640.md) at `0x009F18DD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x009F1C8E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009F1CA9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009F1CCF` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x009F1D16` → [Feature_3609177402__private_IsEnabledDeviceUsageNoInline](../../text/58/Feature_3609177402__private_IsEnabledDeviceUsageNoInline_function_00581D30.md) (`PAGE` → `.text`)
  - `0x009F1D2D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009F1C74  40 53                           push rbx
009F1C76  48 83 EC 30                     sub rsp, 0x30
009F1C7A  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
009F1C80  BA C0 00 00 00                  mov edx, 0xc0
009F1C85  8D 4A 60                        lea ecx, [rdx + 0x60]
009F1C88  41 B8 46 53 72 6F               mov r8d, 0x6f725346
009F1C8E  E8 5D 04 19 00                  call 0x140b820f0
009F1C93  48 8B D8                        mov rbx, rax
009F1C96  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009F1C9B  BA 38 00 00 00                  mov edx, 0x38
009F1CA0  8D 4A 28                        lea ecx, [rdx + 0x28]
009F1CA3  41 B8 46 53 72 6F               mov r8d, 0x6f725346
009F1CA9  E8 42 04 19 00                  call 0x140b820f0
009F1CAE  48 89 83 98 00 00 00            mov qword ptr [rbx + 0x98], rax
009F1CB5  C7 00 01 00 00 00               mov dword ptr [rax], 1
009F1CBB  48 83 60 08 00                  and qword ptr [rax + 8], 0
009F1CC0  83 60 10 00                     and dword ptr [rax + 0x10], 0
009F1CC4  48 8D 48 18                     lea rcx, [rax + 0x18]
009F1CC8  45 33 C0                        xor r8d, r8d
009F1CCB  41 8D 50 01                     lea edx, [r8 + 1]
009F1CCF  E8 3C C0 A1 FF                  call 0x14040dd10
009F1CD4  48 8D 43 28                     lea rax, [rbx + 0x28]
009F1CD8  48 89 40 08                     mov qword ptr [rax + 8], rax
009F1CDC  48 89 00                        mov qword ptr [rax], rax
009F1CDF  48 8D 43 38                     lea rax, [rbx + 0x38]
009F1CE3  48 89 40 08                     mov qword ptr [rax + 8], rax
009F1CE7  48 89 00                        mov qword ptr [rax], rax
009F1CEA  48 8D 43 48                     lea rax, [rbx + 0x48]
009F1CEE  48 89 40 08                     mov qword ptr [rax + 8], rax
009F1CF2  48 89 00                        mov qword ptr [rax], rax
009F1CF5  48 8D 43 58                     lea rax, [rbx + 0x58]
009F1CF9  48 89 40 08                     mov qword ptr [rax + 8], rax
009F1CFD  48 89 00                        mov qword ptr [rax], rax
009F1D00  48 8D 43 68                     lea rax, [rbx + 0x68]
009F1D04  48 89 40 08                     mov qword ptr [rax + 8], rax
009F1D08  48 89 00                        mov qword ptr [rax], rax
009F1D0B  48 8D 43 78                     lea rax, [rbx + 0x78]
009F1D0F  48 89 40 08                     mov qword ptr [rax + 8], rax
009F1D13  48 89 00                        mov qword ptr [rax], rax
009F1D16  E8 15 00 B9 FF                  call 0x140581d30
009F1D1B  85 C0                           test eax, eax
009F1D1D  74 2B                           je 0x1409f1d4a
009F1D1F  BA 10 00 00 00                  mov edx, 0x10
009F1D24  8D 4A 50                        lea ecx, [rdx + 0x50]
009F1D27  41 B8 46 53 72 6F               mov r8d, 0x6f725346
009F1D2D  E8 BE 03 19 00                  call 0x140b820f0
009F1D32  48 89 83 A0 00 00 00            mov qword ptr [rbx + 0xa0], rax
009F1D39  48 89 18                        mov qword ptr [rax], rbx
009F1D3C  48 8B 83 A0 00 00 00            mov rax, qword ptr [rbx + 0xa0]
009F1D43  C7 40 08 00 00 00 00            mov dword ptr [rax + 8], 0
009F1D4A  C7 83 90 00 00 00 01 00 00 00   mov dword ptr [rbx + 0x90], 1
009F1D54  48 8B C3                        mov rax, rbx
009F1D57  48 83 C4 30                     add rsp, 0x30
009F1D5B  5B                              pop rbx
009F1D5C  C3                              ret
009F1D5D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlpAllocateOplock(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (48);
    result = ExAllocatePool2(192 + 96, 192, (unsigned int)(0x6F725346ULL), a4);
    v_stack_m18 = result;
    result = ExAllocatePool2(56 + 40, 56, (unsigned int)(0x6F725346ULL), a4);
    *(unsigned __int64 *)(result + 152) = result;
    *(unsigned int *)(result) = 1;
    a3 = 0;
    result = KeInitializeEvent(result + 24, a3 + 1, a3, a4);
    *(unsigned __int64 *)(result + 40 + 8) = result + 40;
    *(unsigned __int64 *)(result + 40) = result + 40;
    *(unsigned __int64 *)(result + 56 + 8) = result + 56;
    *(unsigned __int64 *)(result + 56) = result + 56;
    *(unsigned __int64 *)(result + 72 + 8) = result + 72;
    *(unsigned __int64 *)(result + 72) = result + 72;
    *(unsigned __int64 *)(result + 88 + 8) = result + 88;
    *(unsigned __int64 *)(result + 88) = result + 88;
    *(unsigned __int64 *)(result + 104 + 8) = result + 104;
    *(unsigned __int64 *)(result + 104) = result + 104;
    *(unsigned __int64 *)(result + 120 + 8) = result + 120;
    *(unsigned __int64 *)(result + 120) = result + 120;
    result = Feature_3609177402__private_IsEnabledDeviceUsageNoInline(result + 24, a3 + 1, a3, a4);
    if ((unsigned int)(result) != 0) {
        a2 = 16;
        a1 = a2 + 80;
        a3 = 0x6F725346ULL;
        result = ExAllocatePool2(a1, a2, a3, a4);
        *(unsigned __int64 *)(result + 160) = result;
        *(unsigned __int64 *)(result) = result;
        result = *(unsigned __int64 *)(result + 160);
        *(unsigned int *)(result + 8) = 0;
    }
    *(unsigned int *)(result + 144) = 1;
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
void FsRtlpAllocateOplock(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (48);
    result = ExAllocatePool2(192 + 96, 192, (uint32_t)(0x6F725346ULL), a4);
    v_stack_m18 = result;
    result = ExAllocatePool2(56 + 40, 56, (uint32_t)(0x6F725346ULL), a4);
    *(uint64_t *)(result + 0x98) = result;
    *(uint32_t *)(result) = 1;
    a3 = 0;
    result = KeInitializeEvent(result + 24, a3 + 1, a3, a4);
    *(uint64_t *)(result + 0x28 + 0x8) = result + 40;
    *(uint64_t *)(result + 0x28) = result + 40;
    *(uint64_t *)(result + 0x38 + 0x8) = result + 56;
    *(uint64_t *)(result + 0x38) = result + 56;
    *(uint64_t *)(result + 0x48 + 0x8) = result + 72;
    *(uint64_t *)(result + 0x48) = result + 72;
    *(uint64_t *)(result + 0x58 + 0x8) = result + 88;
    *(uint64_t *)(result + 0x58) = result + 88;
    *(uint64_t *)(result + 0x68 + 0x8) = result + 104;
    *(uint64_t *)(result + 0x68) = result + 104;
    *(uint64_t *)(result + 0x78 + 0x8) = result + 120;
    *(uint64_t *)(result + 0x78) = result + 120;
    result = Feature_3609177402__private_IsEnabledDeviceUsageNoInline(result + 24, a3 + 1, a3, a4);
    if ((uint32_t)(result) != 0) {
        a2 = 16;
        a1 = a2 + 80;
        a3 = 0x6F725346ULL;
        result = ExAllocatePool2(a1, a2, a3, a4);
        *(uint64_t *)(result + 0xA0) = result;
        *(uint64_t *)(result) = result;
        result = *(uint64_t *)(result + 0xA0);
        *(uint32_t *)(result + 0x8) = 0;
    }
    *(uint32_t *)(result + 0x90) = 1;
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009F1C74&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009F1C74[BB_009F1C74]
  bb_009F1D1F[BB_009F1D1F]
  bb_009F1D4A[BB_009F1D4A]
  bb_009F1D5D[BB_009F1D5D]
  bb_009F1C74 -->|branch| bb_009F1D4A
  bb_009F1C74 -->|fallthrough| bb_009F1D1F
  bb_009F1D1F -->|flow| bb_009F1D4A
```
