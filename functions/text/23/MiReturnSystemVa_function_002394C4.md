# MiReturnSystemVa

- RVA: `0x002394C4`–`0x0023956D` (길이 `169` bytes)
- VA: `0x00000001402394C4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `44`개 명령, `169/169` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00239546` → [MiDecommitSystemPageTables](../2C/MiDecommitSystemPageTables_function_002C1054.md) (function, `0x002C1054`)
- `0x00239557` → [MiMakeSystemRangeAvailable](../4E/MiMakeSystemRangeAvailable_function_004EE174.md) (function, `0x004EE174`)

### Direct callers
- [sub_00237DE0](Unknown_function_00237DE0.md) at `0x00237F32`
- [MiReturnSystemPtes](MiReturnSystemPtes_function_002385C0.md) at `0x00238634`
- [sub_00238945](Unknown_function_00238945.md) at `0x00238B14`
- [MiRemoveFromSystemSpace](../29/MiRemoveFromSystemSpace_function_002962FC.md) at `0x002965CB`
- [MmFreePoolMemory](../2C/MmFreePoolMemory_function_002C1578.md) at `0x002C16C8`
- [MiExpandSystemCache](../3B/MiExpandSystemCache_function_003B3DC8.md) at `0x003B3F21`
- [MiGetPageTablesForLargeMap](../3B/MiGetPageTablesForLargeMap_function_003B48D4.md) at `0x003B49D1`
- [MiExpandPtes](../3B/MiExpandPtes_function_003B4B78.md) at `0x003B4E5F`
- [MiUnmapLargePages](../3F/MiUnmapLargePages_function_003F8BFC.md) at `0x003F8C1E`
- [MiReturnSystemCacheRegionsToKva](../49/MiReturnSystemCacheRegionsToKva_function_00494DFC.md) at `0x00494EB6`
- [MiReleaseLargePdeMappings](../49/MiReleaseLargePdeMappings_function_0049D0B0.md) at `0x0049D2D3`
- [MiDeleteBootRange](../66/MiDeleteBootRange_function_0066E450.md) at `0x0066E65A`
- [MmFreeSecurePoolMemory](../68/MmFreeSecurePoolMemory_function_00682E10.md) at `0x00682EC9`
- [MiReserveDriverPtes](../../page/A7/MiReserveDriverPtes_function_00A75150.md) at `0x00A75314`
- [sub_00B42BDE](../../page/B4/Unknown_function_00B42BDE.md) at `0x00B42BFA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002394C4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002394C9  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
002394CE  57                              push rdi
002394CF  48 83 EC 20                     sub rsp, 0x20
002394D3  48 8B F9                        mov rdi, rcx
002394D6  48 8B DA                        mov rbx, rdx
002394D9  48 C1 EF 09                     shr rdi, 9
002394DD  48 BA F8 FF FF FF 7F 00 00 00   movabs rdx, 0x7ffffffff8
002394E7  48 23 FA                        and rdi, rdx
002394EA  41 8B F0                        mov esi, r8d
002394ED  48 B8 FF 0F 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000fff
002394F7  48 C1 EB 09                     shr rbx, 9
002394FB  48 03 F8                        add rdi, rax
002394FE  48 C7 C1 00 F0 FF FF            mov rcx, 0xfffffffffffff000
00239505  48 23 DA                        and rbx, rdx
00239508  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
00239512  48 23 F9                        and rdi, rcx
00239515  48 8B C2                        mov rax, rdx
00239518  48 03 D8                        add rbx, rax
0023951B  48 23 D9                        and rbx, rcx
0023951E  48 3B FB                        cmp rdi, rbx
00239521  73 39                           jae 0x14023955c
00239523  48 8B C2                        mov rax, rdx
00239526  48 C1 E0 19                     shl rax, 0x19
0023952A  48 C1 E7 19                     shl rdi, 0x19
0023952E  48 C1 E3 19                     shl rbx, 0x19
00239532  48 2B F8                        sub rdi, rax
00239535  48 2B D8                        sub rbx, rax
00239538  48 C1 FF 10                     sar rdi, 0x10
0023953C  48 C1 FB 10                     sar rbx, 0x10
00239540  48 8B CF                        mov rcx, rdi
00239543  48 8B D3                        mov rdx, rbx
00239546  E8 09 7B 08 00                  call 0x1402c1054
0023954B  48 2B DF                        sub rbx, rdi
0023954E  44 8B C6                        mov r8d, esi
00239551  48 8B D3                        mov rdx, rbx
00239554  48 8B CF                        mov rcx, rdi
00239557  E8 18 4C 2B 00                  call 0x1404ee174
0023955C  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00239561  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00239566  48 83 C4 20                     add rsp, 0x20
0023956A  5F                              pop rdi
0023956B  C3                              ret
0023956C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReturnSystemVa(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rdi = (a1) >> (9);
    v_rdi = (v_rdi) & (a2);
    v_rbx = (a2) >> (9);
    v_rdi = (v_rdi) + (result);
    v_rbx = (v_rbx) & (a2);
    v_rdi = (v_rdi) & (0xFFFFFFFFFFFFF000ULL);
    v_rbx = (v_rbx) + (a2);
    v_rbx = (v_rbx) & (0xFFFFFFFFFFFFF000ULL);
    result = a2;
    if (v_rdi < v_rbx) {
        result = a2;
        result = (result) << (25);
        v_rdi = (v_rdi) << (25);
        v_rbx = (v_rbx) << (25);
        v_rdi = (v_rdi) - (result);
        v_rbx = (v_rbx) - (result);
        v_rdi = (v_rdi) >> (16);
        v_rbx = (v_rbx) >> (16);
        a1 = v_rdi;
        a2 = v_rbx;
        result = MiDecommitSystemPageTables(a1, a2, a3, a4);
        v_rbx = (v_rbx) - (v_rdi);
        a3 = (unsigned int)((unsigned int)(a3));
        a2 = v_rbx;
        a1 = v_rdi;
        result = MiMakeSystemRangeAvailable(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiReturnSystemVa(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rdi = (Arg1) >> (9);
    local_rdi = (local_rdi) & (Arg2);
    local_rbx = (Arg2) >> (9);
    local_rdi = (local_rdi) + (result);
    local_rbx = (local_rbx) & (Arg2);
    local_rdi = (local_rdi) & (0xFFFFFFFFFFFFF000ULL);
    local_rbx = (local_rbx) + (Arg2);
    local_rbx = (local_rbx) & (0xFFFFFFFFFFFFF000ULL);
    result = Arg2;
    if (local_rdi < local_rbx) {
        result = Arg2;
        result = (result) << (25);
        local_rdi = (local_rdi) << (25);
        local_rbx = (local_rbx) << (25);
        local_rdi = (local_rdi) - (result);
        local_rbx = (local_rbx) - (result);
        local_rdi = (local_rdi) >> (16);
        local_rbx = (local_rbx) >> (16);
        Arg1 = local_rdi;
        Arg2 = local_rbx;
        result = MiDecommitSystemPageTables(Arg1, Arg2, Arg3, a4);
        local_rbx = (local_rbx) - (local_rdi);
        Arg3 = (uint32_t)((uint32_t)(Arg3));
        Arg2 = local_rbx;
        Arg1 = local_rdi;
        result = MiMakeSystemRangeAvailable(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002394C4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002394C4[BB_002394C4]
  bb_00239523[BB_00239523]
  bb_0023955C[BB_0023955C]
  bb_0023956C[BB_0023956C]
  bb_002394C4 -->|branch| bb_0023955C
  bb_002394C4 -->|fallthrough| bb_00239523
  bb_00239523 -->|flow| bb_0023955C
```
