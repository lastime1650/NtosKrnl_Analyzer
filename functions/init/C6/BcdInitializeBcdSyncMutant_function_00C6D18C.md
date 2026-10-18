# BcdInitializeBcdSyncMutant

- RVA: `0x00C6D18C`–`0x00C6D20B` (길이 `127` bytes)
- VA: `0x0000000140C6D18C`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006EFC0`
- 디코드: `31`개 명령, `127/127` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00C6D1E1` → [ZwCreateMutant](../../text/6A/ZwCreateMutant_function_006AE810.md) (function, `0x006AE810`)
- `0x00C6D1FF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [Phase1InitializationDiscard](../C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1D2FB`

### Static image references
- `0x00C6D19A` → RVA `0x0000C218` (`.rdata`; read)
- `0x00C6D1C3` → RVA `0x00C828C0` (`BiBcdMutantDescriptor`; read)
- `0x00C6D1F0` → RVA `0x00EF05E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00C6D1E1` → [ZwCreateMutant](../../text/6A/ZwCreateMutant_function_006AE810.md) (`INIT` → `.text`)
  - `0x00C6D1FF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C6D18C  40 55                           push rbp
00C6D18E  48 8B EC                        mov rbp, rsp
00C6D191  48 83 EC 50                     sub rsp, 0x50
00C6D195  48 83 65 10 00                  and qword ptr [rbp + 0x10], 0
00C6D19A  48 8D 05 77 F0 39 FF            lea rax, [rip - 0xc60f89]
00C6D1A1  83 65 EC 00                     and dword ptr [rbp - 0x14], 0
00C6D1A5  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00C6D1A9  48 83 65 D8 00                  and qword ptr [rbp - 0x28], 0
00C6D1AE  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00C6D1B2  48 83 65 F8 00                  and qword ptr [rbp - 8], 0
00C6D1B7  45 33 C9                        xor r9d, r9d
00C6D1BA  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00C6D1BE  BA 01 00 1F 00                  mov edx, 0x1f0001
00C6D1C3  48 8D 05 F6 56 01 00            lea rax, [rip + 0x156f6]
00C6D1CA  48 C7 45 D0 30 00 00 00         mov qword ptr [rbp - 0x30], 0x30
00C6D1D2  83 65 D4 00                     and dword ptr [rbp - 0x2c], 0
00C6D1D6  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00C6D1DA  C7 45 E8 50 02 00 00            mov dword ptr [rbp - 0x18], 0x250
00C6D1E1  E8 2A 16 A4 FF                  call 0x1406ae810
00C6D1E6  85 C0                           test eax, eax
00C6D1E8  78 1A                           js 0x140c6d204
00C6D1EA  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00C6D1EE  33 C0                           xor eax, eax
00C6D1F0  F0 48 0F B1 0D E7 33 28 00      lock cmpxchg qword ptr [rip + 0x2833e7], rcx
00C6D1F9  74 09                           je 0x140c6d204
00C6D1FB  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00C6D1FF  E8 AC 00 A4 FF                  call 0x1406ad2b0
00C6D204  48 83 C4 50                     add rsp, 0x50
00C6D208  5D                              pop rbp
00C6D209  C3                              ret
00C6D20A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BcdInitializeBcdSyncMutant(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m34;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (80);
    a4 = 0;
    v_stack_m28 = v_rip - 12980105;
    v_stack_m38 = 48;
    v_stack_m18 = v_rip + 87798;
    v_stack_m20 = 592;
    result = ZwCreateMutant(v_stack_p8, (unsigned int)(0x1F0001ULL), v_stack_m38, a4);
    if (sign_flag) goto loc_00C6D204;
    result = 0;
    if (!(condition_is_equal)) {
        a1 = v_stack_p8;
        result = ZwClose(a1, (unsigned int)(0x1F0001ULL), v_stack_m38, a4);
    }
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t BcdInitializeBcdSyncMutant(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m34;
    uint64_t v_stack_m38;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (80);
    Arg4 = 0;
    v_stack_m28 = v_rip - 12980105;
    v_stack_m38 = 48;
    v_stack_m18 = v_rip + 87798;
    v_stack_m20 = 592;
    result = ZwCreateMutant(v_stack_p8, (uint32_t)(0x1F0001ULL), v_stack_m38, Arg4);
    if (sign_flag) goto loc_00C6D204;
    result = 0;
    if (!(condition_is_equal)) {
        Arg1 = v_stack_p8;
        result = ZwClose(Arg1, (uint32_t)(0x1F0001ULL), v_stack_m38, Arg4);
    }
    local_rsp = (local_rsp) + (80);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C6D18C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C6D18C[BB_00C6D18C]
  bb_00C6D1EA[BB_00C6D1EA]
  bb_00C6D1FB[BB_00C6D1FB]
  bb_00C6D204[BB_00C6D204]
  bb_00C6D20A[BB_00C6D20A]
  bb_00C6D18C -->|branch| bb_00C6D204
  bb_00C6D18C -->|fallthrough| bb_00C6D1EA
  bb_00C6D1EA -->|branch| bb_00C6D204
  bb_00C6D1EA -->|fallthrough| bb_00C6D1FB
  bb_00C6D1FB -->|flow| bb_00C6D204
```
