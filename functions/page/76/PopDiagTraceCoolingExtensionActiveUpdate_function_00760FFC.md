# PopDiagTraceCoolingExtensionActiveUpdate

- RVA: `0x00760FFC`–`0x007610AD` (길이 `177` bytes)
- VA: `0x0000000140760FFC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00087EC4`
- 디코드: `40`개 명령, `177/177` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0076102B` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00761094` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x007610A1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopPropogateCoolingChange](../../text/4E/PopPropogateCoolingChange_function_004E8FA0.md) at `0x004E9082`
- [PopPropogateCoolingChangeV2](../../text/5D/PopPropogateCoolingChangeV2_function_005D1058.md) at `0x005D1183`

### Static image references
- `0x00761002` → RVA `0x00E0A740` (`.data`; read)
- `0x00761011` → RVA `0x00E67858` (`.data`; read)
- `0x0076101D` → RVA `0x00F0B408` (`.data`; read)
- `0x00761024` → RVA `0x00023490` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0076102B` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00761094` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x007610A1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00760FFC  40 53                           push rbx
00760FFE  48 83 EC 70                     sub rsp, 0x70
00761002  48 8B 05 37 97 6A 00            mov rax, qword ptr [rip + 0x6a9737]
00761009  48 33 C4                        xor rax, rsp
0076100C  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00761011  80 3D 40 68 70 00 00            cmp byte ptr [rip + 0x706840], 0
00761018  48 8B D9                        mov rbx, rcx
0076101B  74 7C                           je 0x140761099
0076101D  48 8B 0D E4 A3 7A 00            mov rcx, qword ptr [rip + 0x7aa3e4]
00761024  48 8D 15 65 24 8C FF            lea rdx, [rip - 0x73db9b]
0076102B  E8 20 14 C3 FF                  call 0x140392450
00761030  84 C0                           test al, al
00761032  74 65                           je 0x140761099
00761034  48 8B 0D CD A3 7A 00            mov rcx, qword ptr [rip + 0x7aa3cd]
0076103B  48 8D 15 4E 24 8C FF            lea rdx, [rip - 0x73dbb2]
00761042  33 C0                           xor eax, eax
00761044  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
00761049  38 43 51                        cmp byte ptr [rbx + 0x51], al
0076104C  41 B9 02 00 00 00               mov r9d, 2
00761052  C7 44 24 48 04 00 00 00         mov dword ptr [rsp + 0x48], 4
0076105A  0F 95 C0                        setne al
0076105D  C7 44 24 58 08 00 00 00         mov dword ptr [rsp + 0x58], 8
00761065  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
0076106A  45 33 C0                        xor r8d, r8d
0076106D  83 64 24 5C 00                  and dword ptr [rsp + 0x5c], 0
00761072  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00761076  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0076107B  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00761080  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00761085  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0076108A  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0076108F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00761094  E8 87 B6 CB FF                  call 0x14041c720
00761099  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0076109E  48 33 CC                        xor rcx, rsp
007610A1  E8 9A B5 F4 FF                  call 0x1406ac640
007610A6  48 83 C4 70                     add rsp, 0x70
007610AA  5B                              pop rbx
007610AB  C3                              ret
007610AC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceCoolingExtensionActiveUpdate(__int64 a1, __int64 a2, int a3)
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
    unsigned __int64 v_stack_m58;

    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 6985527)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 7366720)) == 0) goto loc_00761099;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 8037348), v_rip - 7592859, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 8037325);
        a2 = v_rip - 7592882;
        result = 0;
        v_stack_m40 = a1;
        a4 = 2;
        v_stack_m30 = 4;
        result = ((*(unsigned __int8 *)(a1 + 81)) != 0) ? 1 : 0;
        v_stack_m20 = 8;
        a3 = 0;
        v_stack_m48 = (unsigned int)(result);
        result = v_stack_m48;
        v_stack_m38 = result;
        result = v_stack_m40;
        v_stack_m28 = result;
        result = v_stack_m38;
        v_stack_m58 = result;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (112);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceCoolingExtensionActiveUpdate(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

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
    uint64_t v_stack_m58;

    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0x6A9737)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x706840)) == 0) goto loc_00761099;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x7AA3E4), v_rip - 7592859, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0x7AA3CD);
        Arg2 = v_rip - 7592882;
        result = 0;
        v_stack_m40 = Arg1;
        a4 = 2;
        v_stack_m30 = 4;
        result = ((*(uint8_t *)(arg1 + 0x51)) != 0) ? 1 : 0;
        v_stack_m20 = 8;
        Arg3 = 0;
        v_stack_m48 = (uint32_t)(result);
        result = v_stack_m48;
        v_stack_m38 = result;
        result = v_stack_m40;
        v_stack_m28 = result;
        result = v_stack_m38;
        v_stack_m58 = result;
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (112);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x51` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00760FFC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00760FFC[BB_00760FFC]
  bb_0076101D[BB_0076101D]
  bb_00761034[BB_00761034]
  bb_00761099[BB_00761099]
  bb_007610AC[BB_007610AC]
  bb_00760FFC -->|branch| bb_00761099
  bb_00760FFC -->|fallthrough| bb_0076101D
  bb_0076101D -->|branch| bb_00761099
  bb_0076101D -->|fallthrough| bb_00761034
  bb_00761034 -->|flow| bb_00761099
```
