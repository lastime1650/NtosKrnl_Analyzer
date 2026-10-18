# PopDiagTracePowerRequestClose

- RVA: `0x009131A0`–`0x00913228` (길이 `136` bytes)
- VA: `0x00000001409131A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A3CC`
- 디코드: `29`개 명령, `136/136` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x009131CF` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00913210` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x0091321D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopPowerRequestDelete](PopPowerRequestDelete_function_00913030.md) at `0x009130E1`

### Static image references
- `0x009131A9` → RVA `0x00E0A740` (`.data`; read)
- `0x009131B8` → RVA `0x00E67858` (`.data`; read)
- `0x009131C1` → RVA `0x00F0B408` (`.data`; read)
- `0x009131C8` → RVA `0x00011A38` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x009131CF` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00913210` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x0091321D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009131A0  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
009131A5  48 83 EC 58                     sub rsp, 0x58
009131A9  48 8B 05 90 75 4F 00            mov rax, qword ptr [rip + 0x4f7590]
009131B0  48 33 C4                        xor rax, rsp
009131B3  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009131B8  80 3D 99 46 55 00 00            cmp byte ptr [rip + 0x554699], 0
009131BF  74 54                           je 0x140913215
009131C1  48 8B 0D 40 82 5F 00            mov rcx, qword ptr [rip + 0x5f8240]
009131C8  48 8D 15 69 E8 6F FF            lea rdx, [rip - 0x901797]
009131CF  E8 7C F2 A7 FF                  call 0x140392450
009131D4  84 C0                           test al, al
009131D6  74 3D                           je 0x140913215
009131D8  83 64 24 3C 00                  and dword ptr [rsp + 0x3c], 0
009131DD  48 8D 44 24 60                  lea rax, [rsp + 0x60]
009131E2  48 8B 0D 1F 82 5F 00            mov rcx, qword ptr [rip + 0x5f821f]
009131E9  48 8D 15 48 E8 6F FF            lea rdx, [rip - 0x9017b8]
009131F0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009131F5  41 B9 01 00 00 00               mov r9d, 1
009131FB  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00913200  C7 44 24 38 08 00 00 00         mov dword ptr [rsp + 0x38], 8
00913208  45 33 C0                        xor r8d, r8d
0091320B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00913210  E8 0B 95 B0 FF                  call 0x14041c720
00913215  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0091321A  48 33 CC                        xor rcx, rsp
0091321D  E8 1E 94 D9 FF                  call 0x1406ac640
00913222  48 83 C4 58                     add rsp, 0x58
00913226  C3                              ret
00913227  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTracePowerRequestClose(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 5207440)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 5588633)) == 0) goto loc_00913215;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 6259264), v_rip - 9443223, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a1 = *(unsigned __int64 *)(v_rip + 6259231);
        a2 = v_rip - 9443256;
        v_stack_m28 = result;
        a4 = 1;
        result = v_stack_m28;
        v_stack_m20 = 8;
        a3 = 0;
        v_stack_m38 = result;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTracePowerRequestClose(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0x4F7590)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x554699)) == 0) goto loc_00913215;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x5F8240), v_rip - 9443223, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg1 = *(uint64_t *)(v_rip + 0x5F821F);
        Arg2 = v_rip - 9443256;
        v_stack_m28 = result;
        a4 = 1;
        result = v_stack_m28;
        v_stack_m20 = 8;
        Arg3 = 0;
        v_stack_m38 = result;
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009131A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009131A0[BB_009131A0]
  bb_009131C1[BB_009131C1]
  bb_009131D8[BB_009131D8]
  bb_00913215[BB_00913215]
  bb_00913227[BB_00913227]
  bb_009131A0 -->|branch| bb_00913215
  bb_009131A0 -->|fallthrough| bb_009131C1
  bb_009131C1 -->|branch| bb_00913215
  bb_009131C1 -->|fallthrough| bb_009131D8
  bb_009131D8 -->|flow| bb_00913215
```
