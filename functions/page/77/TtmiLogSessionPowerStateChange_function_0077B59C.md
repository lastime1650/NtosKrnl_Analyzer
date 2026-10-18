# TtmiLogSessionPowerStateChange

- RVA: `0x0077B59C`–`0x0077B668` (길이 `204` bytes)
- VA: `0x000000014077B59C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000986F8`
- 디코드: `42`개 명령, `204/204` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0077B5D2` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077B5EB` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x0077B649` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0077B659` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmNotifySessionPowerStateChange](../98/TtmNotifySessionPowerStateChange_function_0098A8F4.md) at `0x0098A92E`

### Static image references
- `0x0077B5A5` → RVA `0x00E0A740` (`.data`; read)
- `0x0077B5B7` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0077B63A` → RVA `0x00052060` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x0077B5D2` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077B5EB` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x0077B649` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0077B659` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077B59C  40 53                           push rbx
0077B59E  48 81 EC 90 00 00 00            sub rsp, 0x90
0077B5A5  48 8B 05 94 F1 68 00            mov rax, qword ptr [rip + 0x68f194]
0077B5AC  48 33 C4                        xor rax, rsp
0077B5AF  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0077B5B7  83 3D 0A D3 85 00 05            cmp dword ptr [rip + 0x85d30a], 5
0077B5BE  8A D9                           mov bl, cl
0077B5C0  0F 86 88 00 00 00               jbe 0x14077b64e
0077B5C6  BA 01 00 00 00                  mov edx, 1
0077B5CB  48 8D 0D F6 D2 85 00            lea rcx, [rip + 0x85d2f6]
0077B5D2  E8 C9 34 CB FF                  call 0x14042eaa0
0077B5D7  84 C0                           test al, al
0077B5D9  74 73                           je 0x14077b64e
0077B5DB  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0077B5E4  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
0077B5EB  E8 00 43 AB FF                  call 0x14022f8f0
0077B5F0  83 64 24 6C 00                  and dword ptr [rsp + 0x6c], 0
0077B5F5  48 8D 0D CC D2 85 00            lea rcx, [rip + 0x85d2cc]
0077B5FC  83 64 24 7C 00                  and dword ptr [rsp + 0x7c], 0
0077B601  BA 04 00 00 00                  mov edx, 4
0077B606  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0077B60A  45 33 C9                        xor r9d, r9d
0077B60D  48 8D 44 24 34                  lea rax, [rsp + 0x34]
0077B612  89 54 24 68                     mov dword ptr [rsp + 0x68], edx
0077B616  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0077B61B  45 33 C0                        xor r8d, r8d
0077B61E  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0077B623  88 5C 24 30                     mov byte ptr [rsp + 0x30], bl
0077B627  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0077B62C  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0077B631  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0077B636  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
0077B63A  48 8D 15 1F 6A 8D FF            lea rdx, [rip - 0x7295e1]
0077B641  C7 44 24 78 01 00 00 00         mov dword ptr [rsp + 0x78], 1
0077B649  E8 92 AA CA FF                  call 0x1404260e0
0077B64E  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
0077B656  48 33 CC                        xor rcx, rsp
0077B659  E8 E2 0F F3 FF                  call 0x1406ac640
0077B65E  48 81 C4 90 00 00 00            add rsp, 0x90
0077B665  5B                              pop rbx
0077B666  C3                              ret
0077B667  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogSessionPowerStateChange(unsigned __int8 a1, __int64 a2, int a3, int a4)
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
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m64;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;

    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 6877588)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 8770314)) <= 5) goto loc_0077B64E;
    result = tlgKeywordOn(v_rip + 8770294, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(a1 + 184);
        result = PsGetProcessSessionIdEx(a1, 1, a3, a4);
        a1 = v_rip + 8770252;
        a2 = 4;
        v_stack_m64 = (unsigned int)(result);
        a4 = 0;
        result = v_stack_m64;
        v_stack_m30 = (unsigned int)(a2);
        v_stack_m38 = result;
        a3 = 0;
        result = v_stack_m68;
        v_stack_m68 = a1;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m70 = result;
        v_stack_m78 = (unsigned int)(a2);
        a2 = v_rip - 7509473;
        v_stack_m20 = 1;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (144);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogSessionPowerStateChange(uint8_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
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
    uint64_t v_stack_m58;
    uint32_t v_stack_m64;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;

    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x68F194)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x85D30A)) <= 5) goto loc_0077B64E;
    result = tlgKeywordOn(v_rip + 8770294, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(Arg1 + 0xB8);
        result = PsGetProcessSessionIdEx(Arg1, 1, Arg3, Arg4);
        Arg1 = v_rip + 8770252;
        Arg2 = 4;
        v_stack_m64 = (uint32_t)(result);
        Arg4 = 0;
        result = v_stack_m64;
        v_stack_m30 = (uint32_t)(Arg2);
        v_stack_m38 = result;
        Arg3 = 0;
        result = v_stack_m68;
        v_stack_m68 = Arg1;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m70 = result;
        v_stack_m78 = (uint32_t)(Arg2);
        Arg2 = v_rip - 7509473;
        v_stack_m20 = 1;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (144);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077B59C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077B59C[BB_0077B59C]
  bb_0077B5C6[BB_0077B5C6]
  bb_0077B5DB[BB_0077B5DB]
  bb_0077B64E[BB_0077B64E]
  bb_0077B667[BB_0077B667]
  bb_0077B59C -->|branch| bb_0077B64E
  bb_0077B59C -->|fallthrough| bb_0077B5C6
  bb_0077B5C6 -->|branch| bb_0077B64E
  bb_0077B5C6 -->|fallthrough| bb_0077B5DB
  bb_0077B5DB -->|flow| bb_0077B64E
```
