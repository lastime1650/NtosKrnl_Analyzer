# PopDiagTraceFxDeviceStartPowerManagement

- RVA: `0x00761610`–`0x007616A6` (길이 `150` bytes)
- VA: `0x0000000140761610`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B3A94`
- 디코드: `33`개 명령, `150/150` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00761631` → [PopFxAddLogEntry](../../text/39/PopFxAddLogEntry_function_00390B94.md) (function, `0x00390B94`)
- `0x0076164D` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x0076168E` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x0076169B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_006FBB10](../../text/6F/Unknown_function_006FBB10.md) at `0x006FBBC1`

### Static image references
- `0x00761614` → RVA `0x00E0A740` (`.data`; read)
- `0x00761636` → RVA `0x00E67858` (`.data`; read)
- `0x0076163F` → RVA `0x00F0B408` (`.data`; read)
- `0x00761646` → RVA `0x00022B78` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00761631` → [PopFxAddLogEntry](../../text/39/PopFxAddLogEntry_function_00390B94.md) (`PAGE` → `.text`)
  - `0x0076164D` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x0076168E` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x0076169B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00761610  48 83 EC 58                     sub rsp, 0x58
00761614  48 8B 05 25 91 6A 00            mov rax, qword ptr [rip + 0x6a9125]
0076161B  48 33 C4                        xor rax, rsp
0076161E  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00761623  45 33 C9                        xor r9d, r9d
00761626  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0076162B  33 D2                           xor edx, edx
0076162D  45 8D 41 03                     lea r8d, [r9 + 3]
00761631  E8 5E F5 C2 FF                  call 0x140390b94
00761636  44 38 0D 1B 62 70 00            cmp byte ptr [rip + 0x70621b], r9b
0076163D  74 54                           je 0x140761693
0076163F  48 8B 0D C2 9D 7A 00            mov rcx, qword ptr [rip + 0x7a9dc2]
00761646  48 8D 15 2B 15 8C FF            lea rdx, [rip - 0x73ead5]
0076164D  E8 FE 0D C3 FF                  call 0x140392450
00761652  84 C0                           test al, al
00761654  74 3D                           je 0x140761693
00761656  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
0076165B  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00761660  48 8B 0D A1 9D 7A 00            mov rcx, qword ptr [rip + 0x7a9da1]
00761667  48 8D 15 0A 15 8C FF            lea rdx, [rip - 0x73eaf6]
0076166E  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00761673  41 B9 01 00 00 00               mov r9d, 1
00761679  48 8D 44 24 38                  lea rax, [rsp + 0x38]
0076167E  C7 44 24 40 08 00 00 00         mov dword ptr [rsp + 0x40], 8
00761686  45 33 C0                        xor r8d, r8d
00761689  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0076168E  E8 8D B0 CB FF                  call 0x14041c720
00761693  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00761698  48 33 CC                        xor rcx, rsp
0076169B  E8 A0 AF F4 FF                  call 0x1406ac640
007616A0  48 83 C4 58                     add rsp, 0x58
007616A4  C3                              ret
007616A5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceFxDeviceStartPowerManagement(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 6983973)) ^ (v_rsp);
    v_stack_m10 = result;
    a4 = 0;
    v_stack_m28 = a1;
    a2 = 0;
    result = PopFxAddLogEntry(a1, a2, a4 + 3, a4);
    if ((*(unsigned __int8 *)(v_rip + 7365147)) == 0) goto loc_00761693;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 8035778), v_rip - 7596757, a4 + 3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m28;
        a1 = *(unsigned __int64 *)(v_rip + 8035745);
        a2 = v_rip - 7596790;
        v_stack_m20 = result;
        a4 = 1;
        result = v_stack_m20;
        v_stack_m18 = 8;
        a3 = 0;
        v_stack_m38 = result;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceFxDeviceStartPowerManagement(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0x6A9125)) ^ (local_rsp);
    v_stack_m10 = result;
    Arg4 = 0;
    v_stack_m28 = Arg1;
    Arg2 = 0;
    result = PopFxAddLogEntry(Arg1, Arg2, Arg4 + 3, Arg4);
    if ((*(uint8_t *)(v_rip + 0x70621B)) == 0) goto loc_00761693;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x7A9DC2), v_rip - 7596757, Arg4 + 3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m28;
        Arg1 = *(uint64_t *)(v_rip + 0x7A9DA1);
        Arg2 = v_rip - 7596790;
        v_stack_m20 = result;
        Arg4 = 1;
        result = v_stack_m20;
        v_stack_m18 = 8;
        Arg3 = 0;
        v_stack_m38 = result;
        result = EtwWrite(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00761610&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00761610[BB_00761610]
  bb_0076163F[BB_0076163F]
  bb_00761656[BB_00761656]
  bb_00761693[BB_00761693]
  bb_007616A5[BB_007616A5]
  bb_00761610 -->|branch| bb_00761693
  bb_00761610 -->|fallthrough| bb_0076163F
  bb_0076163F -->|branch| bb_00761693
  bb_0076163F -->|fallthrough| bb_00761656
  bb_00761656 -->|flow| bb_00761693
```
