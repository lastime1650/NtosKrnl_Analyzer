# TtmiLogInitCurrentSessionStart

- RVA: `0x0098AC60`–`0x0098ACFF` (길이 `159` bytes)
- VA: `0x000000014098AC60`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000986E4`
- 디코드: `33`개 명령, `159/159` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0098AC88` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0098ACA1` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x0098ACE7` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0098ACF4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmInitCurrentSession](TtmInitCurrentSession_function_0098AA18.md) at `0x0098AA22`

### Static image references
- `0x0098AC64` → RVA `0x00E0A740` (`.data`; read)
- `0x0098AC73` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0098ACAB` → RVA `0x00051D57` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x0098AC88` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0098ACA1` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x0098ACE7` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0098ACF4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0098AC60  48 83 EC 78                     sub rsp, 0x78
0098AC64  48 8B 05 D5 FA 47 00            mov rax, qword ptr [rip + 0x47fad5]
0098AC6B  48 33 C4                        xor rax, rsp
0098AC6E  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0098AC73  83 3D 4E DC 64 00 05            cmp dword ptr [rip + 0x64dc4e], 5
0098AC7A  76 70                           jbe 0x14098acec
0098AC7C  BA 01 00 00 00                  mov edx, 1
0098AC81  48 8D 0D 40 DC 64 00            lea rcx, [rip + 0x64dc40]
0098AC88  E8 13 3E AA FF                  call 0x14042eaa0
0098AC8D  84 C0                           test al, al
0098AC8F  74 5B                           je 0x14098acec
0098AC91  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0098AC9A  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
0098ACA1  E8 4A 4C 8A FF                  call 0x14022f8f0
0098ACA6  83 64 24 64 00                  and dword ptr [rsp + 0x64], 0
0098ACAB  48 8D 15 A5 70 6C FF            lea rdx, [rip - 0x938f5b]
0098ACB2  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0098ACB6  48 8D 0D 0B DC 64 00            lea rcx, [rip + 0x64dc0b]
0098ACBD  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0098ACC2  C7 44 24 60 04 00 00 00         mov dword ptr [rsp + 0x60], 4
0098ACCA  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0098ACCF  45 33 C9                        xor r9d, r9d
0098ACD2  48 8D 44 24 38                  lea rax, [rsp + 0x38]
0098ACD7  45 33 C0                        xor r8d, r8d
0098ACDA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0098ACDF  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
0098ACE7  E8 F4 B3 A9 FF                  call 0x1404260e0
0098ACEC  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0098ACF1  48 33 CC                        xor rcx, rsp
0098ACF4  E8 47 19 D2 FF                  call 0x1406ac640
0098ACF9  48 83 C4 78                     add rsp, 0x78
0098ACFD  C3                              ret
0098ACFE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogInitCurrentSessionStart(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;

    v_rsp = (v_rsp) - (120);
    result = (*(unsigned __int64 *)(v_rip + 4717269)) ^ (v_rsp);
    v_stack_m10 = result;
    if ((*(unsigned int *)(v_rip + 6609998)) <= 5) goto loc_0098ACEC;
    result = tlgKeywordOn(v_rip + 6609984, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(a1 + 184);
        result = PsGetProcessSessionIdEx(a1, 1, a3, a4);
        a2 = v_rip - 9670491;
        v_stack_m48 = (unsigned int)(result);
        a1 = v_rip + 6609931;
        result = v_stack_m48;
        v_stack_m18 = 4;
        v_stack_m20 = result;
        a4 = 0;
        result = v_stack_m40;
        a3 = 0;
        v_stack_m50 = result;
        v_stack_m58 = 3;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogInitCurrentSessionStart(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;

    local_rsp = (local_rsp) - (120);
    result = (*(uint64_t *)(v_rip + 0x47FAD5)) ^ (local_rsp);
    v_stack_m10 = result;
    if ((*(uint32_t *)(v_rip + 0x64DC4E)) <= 5) goto loc_0098ACEC;
    result = tlgKeywordOn(v_rip + 6609984, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(Arg1 + 0xB8);
        result = PsGetProcessSessionIdEx(Arg1, 1, Arg3, Arg4);
        Arg2 = v_rip - 9670491;
        v_stack_m48 = (uint32_t)(result);
        Arg1 = v_rip + 6609931;
        result = v_stack_m48;
        v_stack_m18 = 4;
        v_stack_m20 = result;
        Arg4 = 0;
        result = v_stack_m40;
        Arg3 = 0;
        v_stack_m50 = result;
        v_stack_m58 = 3;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (120);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0098AC60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0098AC60[BB_0098AC60]
  bb_0098AC7C[BB_0098AC7C]
  bb_0098AC91[BB_0098AC91]
  bb_0098ACEC[BB_0098ACEC]
  bb_0098ACFE[BB_0098ACFE]
  bb_0098AC60 -->|branch| bb_0098ACEC
  bb_0098AC60 -->|fallthrough| bb_0098AC7C
  bb_0098AC7C -->|branch| bb_0098ACEC
  bb_0098AC7C -->|fallthrough| bb_0098AC91
  bb_0098AC91 -->|flow| bb_0098ACEC
```
