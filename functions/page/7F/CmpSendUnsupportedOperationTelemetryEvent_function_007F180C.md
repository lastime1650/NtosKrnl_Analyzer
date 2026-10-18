# CmpSendUnsupportedOperationTelemetryEvent

- RVA: `0x007F180C`–`0x007F18D5` (길이 `201` bytes)
- VA: `0x00000001407F180C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009EA9C`
- 디코드: `42`개 명령, `201/201` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x007F184C` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x007F18BA` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x007F18C6` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CmpLogUnsupportedOperation](../9A/CmpLogUnsupportedOperation_function_009AEA40.md) at `0x009AEA7D`
- [CmpFlushUnsupportedOperationTelemetry](../AB/CmpFlushUnsupportedOperationTelemetry_function_00AB77B4.md) at `0x00AB77E8`

### Static image references
- `0x007F181A` → RVA `0x00E0A740` (`.data`; read)
- `0x007F1828` → RVA `0x00E09F58` (`.data`; read)
- `0x007F1861` → RVA `0x00057396` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x007F184C` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x007F18BA` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x007F18C6` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007F180C  40 55                           push rbp
007F180E  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
007F1813  48 81 EC A0 00 00 00            sub rsp, 0xa0
007F181A  48 8B 05 1F 8F 61 00            mov rax, qword ptr [rip + 0x618f1f]
007F1821  48 33 C4                        xor rax, rsp
007F1824  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
007F1828  83 3D 29 87 61 00 05            cmp dword ptr [rip + 0x618729], 5
007F182F  44 8B C2                        mov r8d, edx
007F1832  44 8B C9                        mov r9d, ecx
007F1835  0F 86 84 00 00 00               jbe 0x1407f18bf
007F183B  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
007F1845  48 8D 0D 0C 87 61 00            lea rcx, [rip + 0x61870c]
007F184C  E8 4F D2 C3 FF                  call 0x14042eaa0
007F1851  84 C0                           test al, al
007F1853  74 6A                           je 0x1407f18bf
007F1855  48 8D 45 E7                     lea rax, [rbp - 0x19]
007F1859  44 89 4D E7                     mov dword ptr [rbp - 0x19], r9d
007F185D  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
007F1861  48 8D 15 2E 5B 86 FF            lea rdx, [rip - 0x79a4d2]
007F1868  48 8D 45 EB                     lea rax, [rbp - 0x15]
007F186C  44 89 45 EB                     mov dword ptr [rbp - 0x15], r8d
007F1870  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
007F1874  48 8D 0D DD 86 61 00            lea rcx, [rip + 0x6186dd]
007F187B  48 8D 45 EF                     lea rax, [rbp - 0x11]
007F187F  48 C7 45 1F 04 00 00 00         mov qword ptr [rbp + 0x1f], 4
007F1887  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
007F188B  45 33 C9                        xor r9d, r9d
007F188E  48 8D 45 F7                     lea rax, [rbp - 9]
007F1892  48 C7 45 2F 04 00 00 00         mov qword ptr [rbp + 0x2f], 4
007F189A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007F189F  45 33 C0                        xor r8d, r8d
007F18A2  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
007F18AA  48 C7 45 EF 00 00 00 01         mov qword ptr [rbp - 0x11], 0x1000000
007F18B2  48 C7 45 3F 08 00 00 00         mov qword ptr [rbp + 0x3f], 8
007F18BA  E8 21 48 C3 FF                  call 0x1404260e0
007F18BF  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
007F18C3  48 33 CC                        xor rcx, rsp
007F18C6  E8 75 AD EB FF                  call 0x1406ac640
007F18CB  48 81 C4 A0 00 00 00            add rsp, 0xa0
007F18D2  5D                              pop rbp
007F18D3  C3                              ret
007F18D4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpSendUnsupportedOperationTelemetryEvent(int a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m74;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 6393631)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 6391593)) <= 5) goto loc_007F18BF;
    result = tlgKeywordOn(v_rip + 6391564, a2, (unsigned int)(a2), (unsigned int)(a1));
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m78;
        v_stack_m78 = (unsigned int)((unsigned int)(a1));
        v_stack_m48 = result;
        a2 = v_rip - 7972050;
        result = v_stack_m74;
        v_stack_m74 = (unsigned int)((unsigned int)(a2));
        v_stack_m38 = result;
        a1 = v_rip + 6391517;
        result = v_stack_m70;
        v_stack_m40 = 4;
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m68;
        v_stack_m30 = 4;
        v_stack_m80 = result;
        a3 = 0;
        v_stack_m88 = 5;
        v_stack_m70 = 0x1000000ULL;
        v_stack_m20 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpSendUnsupportedOperationTelemetryEvent(int32_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m74;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x618F1F)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x618729)) <= 5) goto loc_007F18BF;
    result = tlgKeywordOn(v_rip + 6391564, Arg2, (uint32_t)(Arg2), (uint32_t)(Arg1));
    if ((uint8_t)(result) != 0) {
        result = v_stack_m78;
        v_stack_m78 = (uint32_t)((uint32_t)(Arg1));
        v_stack_m48 = result;
        Arg2 = v_rip - 7972050;
        result = v_stack_m74;
        v_stack_m74 = (uint32_t)((uint32_t)(Arg2));
        v_stack_m38 = result;
        Arg1 = v_rip + 6391517;
        result = v_stack_m70;
        v_stack_m40 = 4;
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m68;
        v_stack_m30 = 4;
        v_stack_m80 = result;
        a3 = 0;
        v_stack_m88 = 5;
        v_stack_m70 = 0x1000000ULL;
        v_stack_m20 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, a3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007F180C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007F180C[BB_007F180C]
  bb_007F183B[BB_007F183B]
  bb_007F1855[BB_007F1855]
  bb_007F18BF[BB_007F18BF]
  bb_007F18D4[BB_007F18D4]
  bb_007F180C -->|branch| bb_007F18BF
  bb_007F180C -->|fallthrough| bb_007F183B
  bb_007F183B -->|branch| bb_007F18BF
  bb_007F183B -->|fallthrough| bb_007F1855
  bb_007F1855 -->|flow| bb_007F18BF
```
