# BiUnloadHiveByHandle

- RVA: `0x00A4105C`–`0x00A410EC` (길이 `144` bytes)
- VA: `0x0000000140A4105C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AEA28`
- 디코드: `39`개 명령, `144/144` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A410A0` → [BiGetRegistryValue](../A3/BiGetRegistryValue_function_00A3F3CC.md) (function, `0x00A3F3CC`)
- `0x00A410AA` → [BiCloseKey](../91/BiCloseKey_function_00916A00.md) (function, `0x00916A00`)
- `0x00A410BF` → [BiUnloadHiveByName](BiUnloadHiveByName_function_00A410F4.md) (function, `0x00A410F4`)
- `0x00A410D0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [BcdForciblyUnloadStore](../82/BcdForciblyUnloadStore_function_008232FC.md) at `0x00823372`
- [BiCloseStore](../A3/BiCloseStore_function_00A3C5D8.md) at `0x00A3C64C`
- [sub_00B3A892](../B3/Unknown_function_00B3A892.md) at `0x00B3A8F7`
- [sub_00B3A892](../B3/Unknown_function_00B3A892.md) at `0x00B3A98F`

### Static image references
- `0x00A4107A` → RVA `0x00AFF1D0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A41092` → RVA `0x00B0AC30` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A410D0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A4105C  4C 8B DC                        mov r11, rsp
00A4105F  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00A41063  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
00A41067  57                              push rdi
00A41068  48 83 EC 30                     sub rsp, 0x30
00A4106C  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
00A41071  49 8D 43 18                     lea rax, [r11 + 0x18]
00A41075  49 83 63 20 00                  and qword ptr [r11 + 0x20], 0
00A4107A  4C 8D 05 4F E1 0B 00            lea r8, [rip + 0xbe14f]
00A41081  49 89 43 F0                     mov qword ptr [r11 - 0x10], rax
00A41085  40 8A F2                        mov sil, dl
00A41088  49 8D 43 20                     lea rax, [r11 + 0x20]
00A4108C  41 B9 01 00 00 00               mov r9d, 1
00A41092  48 8D 15 97 9B 0C 00            lea rdx, [rip + 0xc9b97]
00A41099  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00A4109D  48 8B D9                        mov rbx, rcx
00A410A0  E8 27 E3 FF FF                  call 0x140a3f3cc
00A410A5  48 8B CB                        mov rcx, rbx
00A410A8  8B F8                           mov edi, eax
00A410AA  E8 51 59 ED FF                  call 0x140916a00
00A410AF  85 FF                           test edi, edi
00A410B1  78 35                           js 0x140a410e8
00A410B3  8B 54 24 50                     mov edx, dword ptr [rsp + 0x50]
00A410B7  44 8A C6                        mov r8b, sil
00A410BA  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00A410BF  E8 30 00 00 00                  call 0x140a410f4
00A410C4  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00A410C9  BA 42 43 44 4B                  mov edx, 0x4b444342
00A410CE  8B D8                           mov ebx, eax
00A410D0  E8 9B 17 14 00                  call 0x140b82870
00A410D5  8B C3                           mov eax, ebx
00A410D7  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00A410DC  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00A410E1  48 83 C4 30                     add rsp, 0x30
00A410E5  5F                              pop rdi
00A410E6  C3                              ret
00A410E7  CC                              int3
00A410E8  8B C7                           mov eax, edi
00A410EA  EB EB                           jmp 0x140a410d7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BiUnloadHiveByHandle(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 16) = v_rsp + 24;
    *(unsigned __int64 *)(v_rsp - 24) = v_rsp + 32;
    result = BiGetRegistryValue(a1, v_rip + 826263, v_rip + 778575, 1);
    result = BiCloseKey(a1, v_rip + 826263, v_rip + 778575, 1);
    if (sign_flag) goto loc_00A410E8;
    result = BiUnloadHiveByName(v_stack_p20, (unsigned int)(v_stack_p18), a2, 1);
    result = ExFreePoolWithTag(v_stack_p20, (unsigned int)(0x4B444342ULL), a2, 1);
loc_00A410D7:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00A410E8:
    goto loc_00A410D7;
}
```

## 5. (Beta) C Style

```c
int64_t BiUnloadHiveByHandle(int64_t Arg1, uint8_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x10) = local_rsp + 24;
    *(uint64_t *)(local_rsp - 0x18) = local_rsp + 32;
    result = BiGetRegistryValue(Arg1, v_rip + 826263, v_rip + 778575, 1);
    result = BiCloseKey(Arg1, v_rip + 826263, v_rip + 778575, 1);
    if (sign_flag) goto loc_00A410E8;
    result = BiUnloadHiveByName(v_stack_p20, (uint32_t)(v_stack_p18), Arg2, 1);
    result = ExFreePoolWithTag(v_stack_p20, (uint32_t)(0x4B444342ULL), Arg2, 1);
loc_00A410D7:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00A410E8:
    goto loc_00A410D7;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A4105C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A4105C[BB_00A4105C]
  bb_00A410B3[BB_00A410B3]
  bb_00A410D7[BB_00A410D7]
  bb_00A410E7[BB_00A410E7]
  bb_00A410E8[BB_00A410E8]
  bb_00A4105C -->|branch| bb_00A410E8
  bb_00A4105C -->|fallthrough| bb_00A410B3
  bb_00A410B3 -->|flow| bb_00A410D7
  bb_00A410E7 -->|flow| bb_00A410E8
  bb_00A410E8 -->|branch| bb_00A410D7
```
