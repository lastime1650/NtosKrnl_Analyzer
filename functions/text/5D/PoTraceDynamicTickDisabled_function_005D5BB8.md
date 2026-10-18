# PoTraceDynamicTickDisabled

- RVA: `0x005D5BB8`–`0x005D5C53` (길이 `155` bytes)
- VA: `0x00000001405D5BB8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00080A9C`
- 디코드: `33`개 명령, `155/155` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x005D5BEC` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x005D5C3B` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x005D5C48` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KeInitializeClock](../../init/C7/KeInitializeClock_function_00C70C30.md) at `0x00C70CFB`

### Static image references
- `0x005D5BBC` → RVA `0x00E0A740` (`.data`; read)
- `0x005D5BCB` → RVA `0x00E67858` (`.data`; read)
- `0x005D5BD2` → RVA `0x00FC5364` (`ALMOSTRO`; read)
- `0x005D5BDE` → RVA `0x00F0B408` (`.data`; read)
- `0x005D5BE5` → RVA `0x000233E0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D5BB8  48 83 EC 68                     sub rsp, 0x68
005D5BBC  48 8B 05 7D 4B 83 00            mov rax, qword ptr [rip + 0x834b7d]
005D5BC3  48 33 C4                        xor rax, rsp
005D5BC6  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
005D5BCB  80 3D 86 1C 89 00 00            cmp byte ptr [rip + 0x891c86], 0
005D5BD2  8A 05 8C F7 9E 00               mov al, byte ptr [rip + 0x9ef78c]
005D5BD8  88 44 24 40                     mov byte ptr [rsp + 0x40], al
005D5BDC  74 62                           je 0x1405d5c40
005D5BDE  48 8B 0D 23 58 93 00            mov rcx, qword ptr [rip + 0x935823]
005D5BE5  48 8D 15 F4 D7 A4 FF            lea rdx, [rip - 0x5b280c]
005D5BEC  E8 5F C8 DB FF                  call 0x140392450
005D5BF1  84 C0                           test al, al
005D5BF3  74 4B                           je 0x1405d5c40
005D5BF5  83 64 24 54 00                  and dword ptr [rsp + 0x54], 0
005D5BFA  48 8D 44 24 40                  lea rax, [rsp + 0x40]
005D5BFF  48 8B 0D 02 58 93 00            mov rcx, qword ptr [rip + 0x935802]
005D5C06  48 8D 15 D3 D7 A4 FF            lea rdx, [rip - 0x5b282d]
005D5C0D  41 B9 01 00 00 00               mov r9d, 1
005D5C13  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
005D5C18  48 8D 44 24 48                  lea rax, [rsp + 0x48]
005D5C1D  44 89 4C 24 50                  mov dword ptr [rsp + 0x50], r9d
005D5C22  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005D5C27  45 33 C0                        xor r8d, r8d
005D5C2A  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
005D5C2F  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005D5C35  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005D5C3B  E8 90 94 C8 FF                  call 0x14025f0d0
005D5C40  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
005D5C45  48 33 CC                        xor rcx, rsp
005D5C48  E8 F3 69 0D 00                  call 0x1406ac640
005D5C4D  48 83 C4 68                     add rsp, 0x68
005D5C51  C3                              ret
005D5C52  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PoTraceDynamicTickDisabled(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int8 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;

    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 8604541)) ^ (v_rsp);
    v_stack_m10 = result;
    v_stack_m28 = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 10418060));
    if ((*(unsigned __int8 *)(v_rip + 8985734)) == 0) goto loc_005D5C40;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9656355), v_rip - 5974028, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m28;
        a1 = *(unsigned __int64 *)(v_rip + 9656322);
        a2 = v_rip - 5974061;
        a4 = 1;
        v_stack_m20 = result;
        result = v_stack_m20;
        v_stack_m18 = (unsigned int)(a4);
        v_stack_m30 = result;
        a3 = 0;
        v_stack_m38 = (unsigned int)(a4);
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (104);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PoTraceDynamicTickDisabled(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint8_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;

    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0x834B7D)) ^ (local_rsp);
    v_stack_m10 = result;
    v_stack_m28 = (uint8_t)(*(uint8_t *)(v_rip + 0x9EF78C));
    if ((*(uint8_t *)(v_rip + 0x891C86)) == 0) goto loc_005D5C40;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x935823), v_rip - 5974028, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m28;
        Arg1 = *(uint64_t *)(v_rip + 0x935802);
        Arg2 = v_rip - 5974061;
        a4 = 1;
        v_stack_m20 = result;
        result = v_stack_m20;
        v_stack_m18 = (uint32_t)(a4);
        v_stack_m30 = result;
        Arg3 = 0;
        v_stack_m38 = (uint32_t)(a4);
        result = EtwWriteEx(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D5BB8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D5BB8[BB_005D5BB8]
  bb_005D5BDE[BB_005D5BDE]
  bb_005D5BF5[BB_005D5BF5]
  bb_005D5C40[BB_005D5C40]
  bb_005D5C52[BB_005D5C52]
  bb_005D5BB8 -->|branch| bb_005D5C40
  bb_005D5BB8 -->|fallthrough| bb_005D5BDE
  bb_005D5BDE -->|branch| bb_005D5C40
  bb_005D5BDE -->|fallthrough| bb_005D5BF5
  bb_005D5BF5 -->|flow| bb_005D5C40
```
