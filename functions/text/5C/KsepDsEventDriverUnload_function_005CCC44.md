# KsepDsEventDriverUnload

- RVA: `0x005CCC44`–`0x005CCCF8` (길이 `180` bytes)
- VA: `0x00000001405CCC44`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CB5B8`
- 디코드: `38`개 명령, `180/180` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005CCC74` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x005CCCE0` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x005CCCED` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KseDsCallbackHookDriverUnload](KseDsCallbackHookDriverUnload_function_005CC000.md) at `0x005CC02B`
- [KseDsHookDriverUntargeted](KseDsHookDriverUntargeted_function_005CC3B0.md) at `0x005CC3B9`

### Static image references
- `0x005CCC52` → RVA `0x00E0A740` (`.data`; read)
- `0x005CCC61` → RVA `0x00E66CE0` (`.data`; read)
- `0x005CCC6D` → RVA `0x00022950` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CCC44  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
005CCC49  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
005CCC4E  48 83 EC 78                     sub rsp, 0x78
005CCC52  48 8B 05 E7 DA 83 00            mov rax, qword ptr [rip + 0x83dae7]
005CCC59  48 33 C4                        xor rax, rsp
005CCC5C  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
005CCC61  48 8B 0D 78 A0 89 00            mov rcx, qword ptr [rip + 0x89a078]
005CCC68  48 85 C9                        test rcx, rcx
005CCC6B  74 78                           je 0x1405ccce5
005CCC6D  48 8D 15 DC 5C A5 FF            lea rdx, [rip - 0x5aa324]
005CCC74  E8 D7 57 DC FF                  call 0x140392450
005CCC79  84 C0                           test al, al
005CCC7B  74 68                           je 0x1405ccce5
005CCC7D  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
005CCC82  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
005CCC8A  83 64 24 5C 00                  and dword ptr [rsp + 0x5c], 0
005CCC8F  48 8D 15 BA 5C A5 FF            lea rdx, [rip - 0x5aa346]
005CCC96  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
005CCC9B  B9 08 00 00 00                  mov ecx, 8
005CCCA0  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
005CCCA8  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
005CCCAC  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
005CCCB1  45 33 C9                        xor r9d, r9d
005CCCB4  48 8D 44 24 40                  lea rax, [rsp + 0x40]
005CCCB9  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
005CCCBD  48 8B 0D 1C A0 89 00            mov rcx, qword ptr [rip + 0x89a01c]
005CCCC4  45 33 C0                        xor r8d, r8d
005CCCC7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005CCCCC  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
005CCCD4  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005CCCDA  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005CCCE0  E8 EB 23 C9 FF                  call 0x14025f0d0
005CCCE5  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
005CCCEA  48 33 CC                        xor rcx, rsp
005CCCED  E8 4E F9 0D 00                  call 0x1406ac640
005CCCF2  48 83 C4 78                     add rsp, 0x78
005CCCF6  C3                              ret
005CCCF7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepDsEventDriverUnload(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (120);
    result = (*(unsigned __int64 *)(v_rip + 8641255)) ^ (v_rsp);
    v_stack_m18 = result;
    if (*(unsigned __int64 *)(v_rip + 9019512) == 0) goto loc_005CCCE5;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9019512), v_rip - 5940004, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a2 = v_rip - 5940038;
        v_stack_m38 = result;
        a1 = 8;
        result = v_stack_p10;
        v_stack_m30 = (unsigned int)(a1);
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m38;
        v_stack_m20 = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 9019420);
        a3 = 0;
        v_stack_m40 = result;
        v_stack_m48 = 2;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KsepDsEventDriverUnload(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (120);
    result = (*(uint64_t *)(v_rip + 0x83DAE7)) ^ (local_rsp);
    v_stack_m18 = result;
    if (*(uint64_t *)(v_rip + 0x89A078) == 0) goto loc_005CCCE5;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x89A078), v_rip - 5940004, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg2 = v_rip - 5940038;
        v_stack_m38 = result;
        Arg1 = 8;
        result = v_stack_p10;
        v_stack_m30 = (uint32_t)(Arg1);
        v_stack_m28 = result;
        Arg4 = 0;
        result = v_stack_m38;
        v_stack_m20 = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x89A01C);
        Arg3 = 0;
        v_stack_m40 = result;
        v_stack_m48 = 2;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (120);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CCC44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CCC44[BB_005CCC44]
  bb_005CCC6D[BB_005CCC6D]
  bb_005CCC7D[BB_005CCC7D]
  bb_005CCCE5[BB_005CCCE5]
  bb_005CCCF7[BB_005CCCF7]
  bb_005CCC44 -->|branch| bb_005CCCE5
  bb_005CCC44 -->|fallthrough| bb_005CCC6D
  bb_005CCC6D -->|branch| bb_005CCCE5
  bb_005CCC6D -->|fallthrough| bb_005CCC7D
  bb_005CCC7D -->|flow| bb_005CCCE5
```
