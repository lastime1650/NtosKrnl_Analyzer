# PopSqmBatteryUpdate

- RVA: `0x00AC1794`–`0x00AC180D` (길이 `121` bytes)
- VA: `0x0000000140AC1794`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A02F8`
- 디코드: `31`개 명령, `121/121` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AC17AA` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (function, `0x0049BF40`)
- `0x00AC17BD` → [PopSqmCreateDwordStreamEntry](../../text/4D/PopSqmCreateDwordStreamEntry_function_004D9C8C.md) (function, `0x004D9C8C`)
- `0x00AC17CA` → [PopSqmCreateDwordStreamEntry](../../text/4D/PopSqmCreateDwordStreamEntry_function_004D9C8C.md) (function, `0x004D9C8C`)
- `0x00AC17DE` → [PopSqmCreateDwordStreamEntry](../../text/4D/PopSqmCreateDwordStreamEntry_function_004D9C8C.md) (function, `0x004D9C8C`)
- `0x00AC17EB` → [PopSqmCreateDwordStreamEntry](../../text/4D/PopSqmCreateDwordStreamEntry_function_004D9C8C.md) (function, `0x004D9C8C`)
- `0x00AC17F5` → [PopSqmAddToStream](../../text/4A/PopSqmAddToStream_function_004AA044.md) (function, `0x004AA044`)
- `0x00AC1802` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopBatteryApplyCompositeState](../AE/PopBatteryApplyCompositeState_function_00AE0CD0.md) at `0x00AE0EE1`

### Static image references
- `0x00AC1798` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00AC17AA` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (`PAGE` → `.text`)
  - `0x00AC17BD` → [PopSqmCreateDwordStreamEntry](../../text/4D/PopSqmCreateDwordStreamEntry_function_004D9C8C.md) (`PAGE` → `.text`)
  - `0x00AC17CA` → [PopSqmCreateDwordStreamEntry](../../text/4D/PopSqmCreateDwordStreamEntry_function_004D9C8C.md) (`PAGE` → `.text`)
  - `0x00AC17DE` → [PopSqmCreateDwordStreamEntry](../../text/4D/PopSqmCreateDwordStreamEntry_function_004D9C8C.md) (`PAGE` → `.text`)
  - `0x00AC17EB` → [PopSqmCreateDwordStreamEntry](../../text/4D/PopSqmCreateDwordStreamEntry_function_004D9C8C.md) (`PAGE` → `.text`)
  - `0x00AC17F5` → [PopSqmAddToStream](../../text/4A/PopSqmAddToStream_function_004AA044.md) (`PAGE` → `.text`)
  - `0x00AC1802` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AC1794  48 83 EC 78                     sub rsp, 0x78
00AC1798  48 8B 05 A1 8F 34 00            mov rax, qword ptr [rip + 0x348fa1]
00AC179F  48 33 C4                        xor rax, rsp
00AC17A2  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00AC17A7  44 8B DA                        mov r11d, edx
00AC17AA  E8 91 A7 9D FF                  call 0x14049bf40
00AC17AF  45 33 D2                        xor r10d, r10d
00AC17B2  84 C0                           test al, al
00AC17B4  74 44                           je 0x140ac17fa
00AC17B6  8B D1                           mov edx, ecx
00AC17B8  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00AC17BD  E8 CA 84 A1 FF                  call 0x1404d9c8c
00AC17C2  41 8B D3                        mov edx, r11d
00AC17C5  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00AC17CA  E8 BD 84 A1 FF                  call 0x1404d9c8c
00AC17CF  45 85 C0                        test r8d, r8d
00AC17D2  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00AC17D7  41 0F 94 C2                     sete r10b
00AC17DB  41 8B D2                        mov edx, r10d
00AC17DE  E8 A9 84 A1 FF                  call 0x1404d9c8c
00AC17E3  41 8B D1                        mov edx, r9d
00AC17E6  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00AC17EB  E8 9C 84 A1 FF                  call 0x1404d9c8c
00AC17F0  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
00AC17F5  E8 4A 88 9E FF                  call 0x1404aa044
00AC17FA  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00AC17FF  48 33 CC                        xor rcx, rsp
00AC1802  E8 39 AE BE FF                  call 0x1406ac640
00AC1807  48 83 C4 78                     add rsp, 0x78
00AC180B  C3                              ret
00AC180C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopSqmBatteryUpdate(int a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;

    v_rsp = (v_rsp) - (120);
    result = (*(unsigned __int64 *)(v_rip + 3444641)) ^ (v_rsp);
    v_stack_m18 = result;
    result = PopIsPlatformAoAcCapable(a1, a2, a3, a4);
    v_r10 = 0;
    if ((unsigned __int8)(result) != 0) {
        a2 = a1;
        a1 = v_stack_m58;
        result = PopSqmCreateDwordStreamEntry(a1, a2, a3, a4);
        a2 = (unsigned int)((unsigned int)(a2));
        a1 = v_stack_m48;
        result = PopSqmCreateDwordStreamEntry(a1, a2, a3, a4);
        a1 = v_stack_m38;
        v_r10 = (a3 == 0) ? 1 : 0;
        a2 = (unsigned int)(v_r10);
        result = PopSqmCreateDwordStreamEntry(a1, a2, a3, a4);
        a2 = a4;
        a1 = v_stack_m28;
        result = PopSqmCreateDwordStreamEntry(a1, a2, a3, a4);
        a4 = v_stack_m58;
        result = PopSqmAddToStream(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopSqmBatteryUpdate(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;

    local_rsp = (local_rsp) - (120);
    result = (*(uint64_t *)(v_rip + 0x348FA1)) ^ (local_rsp);
    v_stack_m18 = result;
    result = PopIsPlatformAoAcCapable(Arg1, Arg2, Arg3, Arg4);
    local_r10 = 0;
    if ((uint8_t)(result) != 0) {
        Arg2 = Arg1;
        Arg1 = v_stack_m58;
        result = PopSqmCreateDwordStreamEntry(Arg1, Arg2, Arg3, Arg4);
        Arg2 = (uint32_t)((uint32_t)(Arg2));
        Arg1 = v_stack_m48;
        result = PopSqmCreateDwordStreamEntry(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_m38;
        local_r10 = (Arg3 == 0) ? 1 : 0;
        Arg2 = (uint32_t)(local_r10);
        result = PopSqmCreateDwordStreamEntry(Arg1, Arg2, Arg3, Arg4);
        Arg2 = Arg4;
        Arg1 = v_stack_m28;
        result = PopSqmCreateDwordStreamEntry(Arg1, Arg2, Arg3, Arg4);
        Arg4 = v_stack_m58;
        result = PopSqmAddToStream(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (120);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AC1794&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AC1794[BB_00AC1794]
  bb_00AC17B6[BB_00AC17B6]
  bb_00AC17FA[BB_00AC17FA]
  bb_00AC180C[BB_00AC180C]
  bb_00AC1794 -->|branch| bb_00AC17FA
  bb_00AC1794 -->|fallthrough| bb_00AC17B6
  bb_00AC17B6 -->|flow| bb_00AC17FA
```
