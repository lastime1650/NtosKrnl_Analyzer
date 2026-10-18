# BiIsWinPEBoot

- RVA: `0x00A40F54`–`0x00A40FD0` (길이 `124` bytes)
- VA: `0x0000000140A40F54`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000ADBB4`
- 디코드: `33`개 명령, `124/124` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00A40F8E` → [BiGetRegistryValue](../A3/BiGetRegistryValue_function_00A3F3CC.md) (function, `0x00A3F3CC`)
- `0x00A40FA3` → [wcsstr](../../text/50/wcsstr_function_00501F80.md) (function, `0x00501F80`)
- `0x00A40FB5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [BcdCloseStore](../A3/BcdCloseStore_function_00A3C68C.md) at `0x00A3C724`
- [BiOpenSystemStore](BiOpenSystemStore_function_00A40844.md) at `0x00A408A0`

### Static image references
- `0x00A40F6A` → RVA `0x00B0C260` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A40F79` → RVA `0x00B0C1A0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A40F9C` → RVA `0x00B0C1D0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A40FA3` → [wcsstr](../../text/50/wcsstr_function_00501F80.md) (`PAGE` → `.text`)
  - `0x00A40FB5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A40F54  4C 8B DC                        mov r11, rsp
00A40F57  49 89 5B 18                     mov qword ptr [r11 + 0x18], rbx
00A40F5B  57                              push rdi
00A40F5C  48 83 EC 30                     sub rsp, 0x30
00A40F60  33 FF                           xor edi, edi
00A40F62  49 8D 43 08                     lea rax, [r11 + 8]
00A40F66  49 89 43 F0                     mov qword ptr [r11 - 0x10], rax
00A40F6A  4C 8D 05 EF B2 0C 00            lea r8, [rip + 0xcb2ef]
00A40F71  49 8D 43 10                     lea rax, [r11 + 0x10]
00A40F75  49 89 7B 10                     mov qword ptr [r11 + 0x10], rdi
00A40F79  48 8D 15 20 B2 0C 00            lea rdx, [rip + 0xcb220]
00A40F80  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
00A40F84  44 8D 4F 01                     lea r9d, [rdi + 1]
00A40F88  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00A40F8C  33 C9                           xor ecx, ecx
00A40F8E  E8 39 E4 FF FF                  call 0x140a3f3cc
00A40F93  85 C0                           test eax, eax
00A40F95  78 2A                           js 0x140a40fc1
00A40F97  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A40F9C  48 8D 15 2D B2 0C 00            lea rdx, [rip + 0xcb22d]
00A40FA3  E8 D8 0F AC FF                  call 0x140501f80
00A40FA8  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A40FAD  BA 42 43 44 4B                  mov edx, 0x4b444342
00A40FB2  48 8B D8                        mov rbx, rax
00A40FB5  E8 B6 18 14 00                  call 0x140b82870
00A40FBA  48 85 DB                        test rbx, rbx
00A40FBD  40 0F 95 C7                     setne dil
00A40FC1  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00A40FC6  40 8A C7                        mov al, dil
00A40FC9  48 83 C4 30                     add rsp, 0x30
00A40FCD  5F                              pop rdi
00A40FCE  C3                              ret
00A40FCF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BiIsWinPEBoot(int a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    v_rsp = (v_rsp) - (48);
    v_rdi = 0;
    *(unsigned __int64 *)(v_rsp - 16) = v_rsp + 8;
    *(unsigned __int64 *)(v_rsp + 16) = 0;
    v_stack_p8 = 0;
    *(unsigned __int64 *)(v_rsp - 24) = v_rsp + 16;
    a1 = 0;
    result = BiGetRegistryValue(a1, v_rip + 832032, v_rip + 832239, v_rdi + 1);
    if (!(sign_flag)) {
        a1 = v_stack_p10;
        a2 = v_rip + 832045;
        result = wcsstr(a1, a2, v_rip + 832239, v_rdi + 1);
        a1 = v_stack_p10;
        a2 = 0x4B444342ULL;
        v_rbx = result;
        result = ExFreePoolWithTag(a1, a2, v_rip + 832239, v_rdi + 1);
        v_rdi = (v_rbx != 0) ? 1 : 0;
    }
    v_rsp = (v_rsp) + (48);
    return (unsigned __int8)(v_rdi);
}
```

## 5. (Beta) C Style

```c
int64_t BiIsWinPEBoot(int32_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    local_rsp = (local_rsp) - (48);
    local_rdi = 0;
    *(uint64_t *)(local_rsp - 0x10) = local_rsp + 8;
    *(uint64_t *)(local_rsp + 0x10) = 0;
    v_stack_p8 = 0;
    *(uint64_t *)(local_rsp - 0x18) = local_rsp + 16;
    Arg1 = 0;
    result = BiGetRegistryValue(Arg1, v_rip + 832032, v_rip + 832239, local_rdi + 1);
    if (!(sign_flag)) {
        Arg1 = v_stack_p10;
        a2 = v_rip + 832045;
        result = wcsstr(Arg1, a2, v_rip + 832239, local_rdi + 1);
        Arg1 = v_stack_p10;
        a2 = 0x4B444342ULL;
        local_rbx = result;
        result = ExFreePoolWithTag(Arg1, a2, v_rip + 832239, local_rdi + 1);
        local_rdi = (local_rbx != 0) ? 1 : 0;
    }
    local_rsp = (local_rsp) + (48);
    return (uint8_t)(local_rdi);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A40F54&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A40F54[BB_00A40F54]
  bb_00A40F97[BB_00A40F97]
  bb_00A40FC1[BB_00A40FC1]
  bb_00A40FCF[BB_00A40FCF]
  bb_00A40F54 -->|branch| bb_00A40FC1
  bb_00A40F54 -->|fallthrough| bb_00A40F97
  bb_00A40F97 -->|flow| bb_00A40FC1
```
