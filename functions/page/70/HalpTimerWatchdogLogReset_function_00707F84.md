# HalpTimerWatchdogLogReset

- RVA: `0x00707F84`–`0x00707FCB` (길이 `71` bytes)
- VA: `0x0000000140707F84`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `17`개 명령, `71/71` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00707F88` → [HalpTimerWatchdogGeneratedLastReset](HalpTimerWatchdogGeneratedLastReset_function_00707F60.md) (function, `0x00707F60`)
- `0x00707FB4` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00707FC0` → [DbgPrint](../../text/35/DbgPrint_function_00358CB0.md) (function, `0x00358CB0`)

### Direct callers
- [HalpTimerInitSystem](../../text/53/HalpTimerInitSystem_function_0053CB70.md) at `0x0053CBFF`

### Static image references
- `0x00707F91` → RVA `0x00FC22C0` (`.data`; read)
- `0x00707F9A` → RVA `0x00FC22B8` (`.data`; read)
- `0x00707FA1` → RVA `0x00022F40` (`.rdata`; read)
- `0x00707FB9` → RVA `0x00023ED8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00707FB4` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00707FC0` → [DbgPrint](../../text/35/DbgPrint_function_00358CB0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00707F84  48 83 EC 38                     sub rsp, 0x38
00707F88  E8 D3 FF FF FF                  call 0x140707f60
00707F8D  84 C0                           test al, al
00707F8F  74 34                           je 0x140707fc5
00707F91  80 3D 28 A3 8B 00 00            cmp byte ptr [rip + 0x8ba328], 0
00707F98  74 2B                           je 0x140707fc5
00707F9A  48 8B 0D 17 A3 8B 00            mov rcx, qword ptr [rip + 0x8ba317]
00707FA1  48 8D 15 98 AF 91 FF            lea rdx, [rip - 0x6e5068]
00707FA8  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00707FAE  45 33 C9                        xor r9d, r9d
00707FB1  45 33 C0                        xor r8d, r8d
00707FB4  E8 67 47 D1 FF                  call 0x14041c720
00707FB9  48 8D 0D 18 BF 91 FF            lea rcx, [rip - 0x6e40e8]
00707FC0  E8 EB 0C C5 FF                  call 0x140358cb0
00707FC5  48 83 C4 38                     add rsp, 0x38
00707FC9  C3                              ret
00707FCA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpTimerWatchdogLogReset(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    result = HalpTimerWatchdogGeneratedLastReset(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00707FC5;
    if ((*(unsigned __int8 *)(v_rip + 9151272)) != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 9151255);
        a2 = v_rip - 7229544;
        a4 = 0;
        a3 = 0;
        result = EtwWrite(a1, a2, a3, a4);
        a1 = v_rip - 7225576;
        result = DbgPrint(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpTimerWatchdogLogReset(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    result = HalpTimerWatchdogGeneratedLastReset(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00707FC5;
    if ((*(uint8_t *)(v_rip + 0x8BA328)) != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0x8BA317);
        Arg2 = v_rip - 7229544;
        Arg4 = 0;
        Arg3 = 0;
        result = EtwWrite(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_rip - 7225576;
        result = DbgPrint(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00707F84&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00707F84[BB_00707F84]
  bb_00707F91[BB_00707F91]
  bb_00707F9A[BB_00707F9A]
  bb_00707FC5[BB_00707FC5]
  bb_00707FCA[BB_00707FCA]
  bb_00707F84 -->|branch| bb_00707FC5
  bb_00707F84 -->|fallthrough| bb_00707F91
  bb_00707F91 -->|branch| bb_00707FC5
  bb_00707F91 -->|fallthrough| bb_00707F9A
  bb_00707F9A -->|flow| bb_00707FC5
```
