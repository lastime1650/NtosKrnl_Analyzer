# MiLogPerfMemoryRangeEvent

- RVA: `0x004D9D7C`–`0x004D9E30` (길이 `180` bytes)
- VA: `0x00000001404D9D7C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009EA50`
- 디코드: `44`개 명령, `180/180` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004D9E17` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x004D9E24` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MiCommitPoolMemory](../32/MiCommitPoolMemory_function_00329520.md) at `0x003297B6`
- [MiDecommitLargePoolVa](../37/MiDecommitLargePoolVa_function_00377DD4.md) at `0x00377EFF`
- [MiMapUserLargePages](../3D/MiMapUserLargePages_function_003D26F4.md) at `0x003D2D97`
- [MiAllocateContiguousMemory](../3E/MiAllocateContiguousMemory_function_003E9FDC.md) at `0x003EA62C`
- [MmFreeContiguousMemory](../3F/MmFreeContiguousMemory_function_003F6F60.md) at `0x003F7168`
- [MiLogSectionCreate](../../page/7F/MiLogSectionCreate_function_007FCDEC.md) at `0x007FCEB8`
- [sub_00B190F2](../../page/B1/Unknown_function_00B190F2.md) at `0x00B191A1`

### Static image references
- `0x004D9D82` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004D9D7C  40 53                           push rbx
004D9D7E  48 83 EC 60                     sub rsp, 0x60
004D9D82  48 8B 05 B7 09 93 00            mov rax, qword ptr [rip + 0x9309b7]
004D9D89  48 33 C4                        xor rax, rsp
004D9D8C  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
004D9D91  4D 8B D9                        mov r11, r9
004D9D94  45 33 D2                        xor r10d, r10d
004D9D97  B8 78 02 00 00                  mov eax, 0x278
004D9D9C  45 0F B7 C8                     movzx r9d, r8w
004D9DA0  66 41 F7 D1                     not r9w
004D9DA4  41 8D 5A 01                     lea ebx, [r10 + 1]
004D9DA8  66 44 23 CB                     and r9w, bx
004D9DAC  66 44 0B C8                     or r9w, ax
004D9DB0  41 8B C0                        mov eax, r8d
004D9DB3  83 E0 1E                        and eax, 0x1e
004D9DB6  3C 1A                           cmp al, 0x1a
004D9DB8  75 14                           jne 0x1404d9dce
004D9DBA  4C 8B D2                        mov r10, rdx
004D9DBD  48 B8 FF FF FF FF FF FF 00 00   movabs rax, 0xffffffffffff
004D9DC7  4C 23 D0                        and r10, rax
004D9DCA  49 C1 E2 04                     shl r10, 4
004D9DCE  83 64 24 54 00                  and dword ptr [rsp + 0x54], 0
004D9DD3  48 8D 44 24 30                  lea rax, [rsp + 0x30]
004D9DD8  49 D1 E8                        shr r8, 1
004D9DDB  49 83 E2 F0                     and r10, 0xfffffffffffffff0
004D9DDF  41 83 E0 0F                     and r8d, 0xf
004D9DE3  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
004D9DE8  4D 0B C2                        or r8, r10
004D9DEB  4C 89 5C 24 40                  mov qword ptr [rsp + 0x40], r11
004D9DF0  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
004D9DF5  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
004D9DFA  41 B8 01 00 00 20               mov r8d, 0x20000001
004D9E00  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
004D9E05  8B D3                           mov edx, ebx
004D9E07  C7 44 24 50 18 00 00 00         mov dword ptr [rsp + 0x50], 0x18
004D9E0F  C7 44 24 20 04 1B 50 11         mov dword ptr [rsp + 0x20], 0x11501b04
004D9E17  E8 34 B5 D5 FF                  call 0x140235350
004D9E1C  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
004D9E21  48 33 CC                        xor rcx, rsp
004D9E24  E8 17 28 1D 00                  call 0x1406ac640
004D9E29  48 83 C4 60                     add rsp, 0x60
004D9E2D  5B                              pop rbx
004D9E2E  C3                              ret
004D9E2F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLogPerfMemoryRangeEvent(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m48;

    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 9636279)) ^ (v_rsp);
    v_stack_m10 = result;
    v_r10 = 0;
    a4 = (unsigned __int16)(~((unsigned __int16)(a3)));
    a4 = (unsigned __int16)((a4) & ((unsigned __int16)(v_r10 + 1)));
    a4 = (unsigned __int16)((a4) | (632));
    result = (unsigned int)(((unsigned int)((unsigned int)(a3))) & (30));
    if (((unsigned __int8)(result)) == 26) {
        v_r10 = a2;
        v_r10 = (v_r10) & (result);
        v_r10 = (v_r10) << (4);
    }
    a3 = (a3) >> (1);
    v_r10 = (v_r10) & (-16);
    a3 = (unsigned int)((a3) & (15));
    v_stack_m30 = a1;
    a3 = (a3) | (v_r10);
    v_stack_m28 = a4;
    v_stack_m38 = a3;
    v_stack_m20 = v_stack_m38;
    v_stack_m18 = 24;
    v_stack_m48 = 0x11501B04ULL;
    result = EtwTraceKernelEvent(v_stack_m20, (unsigned int)((unsigned int)(v_r10 + 1)), (unsigned int)(0x20000001ULL), a4);
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)((unsigned int)(v_r10 + 1)), (unsigned int)(0x20000001ULL), a4);
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiLogPerfMemoryRangeEvent(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m48;

    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0x9309B7)) ^ (local_rsp);
    v_stack_m10 = result;
    local_r10 = 0;
    Arg4 = (uint16_t)(~((uint16_t)(Arg3)));
    Arg4 = (uint16_t)((Arg4) & ((uint16_t)(local_r10 + 1)));
    Arg4 = (uint16_t)((Arg4) | (632));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) & (30));
    if (((uint8_t)(result)) == 26) {
        local_r10 = Arg2;
        local_r10 = (local_r10) & (result);
        local_r10 = (local_r10) << (4);
    }
    Arg3 = (Arg3) >> (1);
    local_r10 = (local_r10) & (-16);
    Arg3 = (uint32_t)((Arg3) & (15));
    v_stack_m30 = Arg1;
    Arg3 = (Arg3) | (local_r10);
    v_stack_m28 = Arg4;
    v_stack_m38 = Arg3;
    v_stack_m20 = v_stack_m38;
    v_stack_m18 = 24;
    v_stack_m48 = 0x11501B04ULL;
    result = EtwTraceKernelEvent(v_stack_m20, (uint32_t)((uint32_t)(local_r10 + 1)), (uint32_t)(0x20000001ULL), Arg4);
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)((uint32_t)(local_r10 + 1)), (uint32_t)(0x20000001ULL), Arg4);
    local_rsp = (local_rsp) + (96);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004D9D7C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004D9D7C[BB_004D9D7C]
  bb_004D9DBA[BB_004D9DBA]
  bb_004D9DCE[BB_004D9DCE]
  bb_004D9E2F[BB_004D9E2F]
  bb_004D9D7C -->|branch| bb_004D9DCE
  bb_004D9D7C -->|fallthrough| bb_004D9DBA
  bb_004D9DBA -->|flow| bb_004D9DCE
```
