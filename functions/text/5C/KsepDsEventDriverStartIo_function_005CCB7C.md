# KsepDsEventDriverStartIo

- RVA: `0x005CCB7C`–`0x005CCC3E` (길이 `194` bytes)
- VA: `0x00000001405CCB7C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BF3D4`
- 디코드: `46`개 명령, `194/194` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005CCBB7` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x005CCC23` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x005CCC2F` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KseDsCallbackHookDriverStartIo](KseDsCallbackHookDriverStartIo_function_005CBFA0.md) at `0x005CBFDC`

### Static image references
- `0x005CCB96` → RVA `0x00E0A740` (`.data`; read)
- `0x005CCBA4` → RVA `0x00E66CE0` (`.data`; read)
- `0x005CCBB0` → RVA `0x00023140` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CCB7C  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
005CCB81  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
005CCB86  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
005CCB8B  55                              push rbp
005CCB8C  48 8B EC                        mov rbp, rsp
005CCB8F  48 81 EC 80 00 00 00            sub rsp, 0x80
005CCB96  48 8B 05 A3 DB 83 00            mov rax, qword ptr [rip + 0x83dba3]
005CCB9D  48 33 C4                        xor rax, rsp
005CCBA0  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
005CCBA4  48 8B 0D 35 A1 89 00            mov rcx, qword ptr [rip + 0x89a135]
005CCBAB  48 85 C9                        test rcx, rcx
005CCBAE  74 78                           je 0x1405ccc28
005CCBB0  48 8D 15 89 65 A5 FF            lea rdx, [rip - 0x5a9a77]
005CCBB7  E8 94 58 DC FF                  call 0x140392450
005CCBBC  84 C0                           test al, al
005CCBBE  74 68                           je 0x1405ccc28
005CCBC0  83 65 CC 00                     and dword ptr [rbp - 0x34], 0
005CCBC4  48 8D 45 10                     lea rax, [rbp + 0x10]
005CCBC8  83 65 DC 00                     and dword ptr [rbp - 0x24], 0
005CCBCC  48 8D 15 6D 65 A5 FF            lea rdx, [rip - 0x5a9a93]
005CCBD3  83 65 EC 00                     and dword ptr [rbp - 0x14], 0
005CCBD7  B9 08 00 00 00                  mov ecx, 8
005CCBDC  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
005CCBE0  45 33 C9                        xor r9d, r9d
005CCBE3  48 8D 45 18                     lea rax, [rbp + 0x18]
005CCBE7  89 4D C8                        mov dword ptr [rbp - 0x38], ecx
005CCBEA  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
005CCBEE  45 33 C0                        xor r8d, r8d
005CCBF1  48 8D 45 20                     lea rax, [rbp + 0x20]
005CCBF5  89 4D D8                        mov dword ptr [rbp - 0x28], ecx
005CCBF8  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
005CCBFC  48 8D 45 C0                     lea rax, [rbp - 0x40]
005CCC00  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005CCC05  C7 44 24 30 03 00 00 00         mov dword ptr [rsp + 0x30], 3
005CCC0D  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005CCC13  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005CCC19  89 4D E8                        mov dword ptr [rbp - 0x18], ecx
005CCC1C  48 8B 0D BD A0 89 00            mov rcx, qword ptr [rip + 0x89a0bd]
005CCC23  E8 A8 24 C9 FF                  call 0x14025f0d0
005CCC28  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
005CCC2C  48 33 CC                        xor rcx, rsp
005CCC2F  E8 0C FA 0D 00                  call 0x1406ac640
005CCC34  48 81 C4 80 00 00 00            add rsp, 0x80
005CCC3B  5D                              pop rbp
005CCC3C  C3                              ret
005CCC3D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepDsEventDriverStartIo(__int64 a1, __int64 a2, __int64 a3, int a4)
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
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 8641443)) ^ (v_rsp);
    v_stack_m18 = result;
    if (*(unsigned __int64 *)(v_rip + 9019701) == 0) goto loc_005CCC28;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9019701), v_rip - 5937783, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a2 = v_rip - 5937811;
        a1 = 8;
        v_stack_m48 = result;
        a4 = 0;
        result = v_stack_p10;
        v_stack_m40 = (unsigned int)(a1);
        v_stack_m38 = result;
        a3 = 0;
        result = v_stack_p18;
        v_stack_m30 = (unsigned int)(a1);
        v_stack_m28 = result;
        result = v_stack_m48;
        v_stack_m50 = result;
        v_stack_m58 = 3;
        v_stack_m20 = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 9019581);
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KsepDsEventDriverStartIo(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
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
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x83DBA3)) ^ (local_rsp);
    v_stack_m18 = result;
    if (*(uint64_t *)(v_rip + 0x89A135) == 0) goto loc_005CCC28;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x89A135), v_rip - 5937783, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg2 = v_rip - 5937811;
        Arg1 = 8;
        v_stack_m48 = result;
        Arg4 = 0;
        result = v_stack_p10;
        v_stack_m40 = (uint32_t)(Arg1);
        v_stack_m38 = result;
        Arg3 = 0;
        result = v_stack_p18;
        v_stack_m30 = (uint32_t)(Arg1);
        v_stack_m28 = result;
        result = v_stack_m48;
        v_stack_m50 = result;
        v_stack_m58 = 3;
        v_stack_m20 = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x89A0BD);
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (128);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CCB7C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CCB7C[BB_005CCB7C]
  bb_005CCBB0[BB_005CCBB0]
  bb_005CCBC0[BB_005CCBC0]
  bb_005CCC28[BB_005CCC28]
  bb_005CCC3D[BB_005CCC3D]
  bb_005CCB7C -->|branch| bb_005CCC28
  bb_005CCB7C -->|fallthrough| bb_005CCBB0
  bb_005CCBB0 -->|branch| bb_005CCC28
  bb_005CCBB0 -->|fallthrough| bb_005CCBC0
  bb_005CCBC0 -->|flow| bb_005CCC28
```
