# PipDmgInitPhaseTwo

- RVA: `0x0073C07C`–`0x0073C0B0` (길이 `52` bytes)
- VA: `0x000000014073C07C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0073C089` → [PipDmgInitReadGroupPolicy](PipDmgInitReadGroupPolicy_function_007309B8.md) (function, `0x007309B8`)
- `0x0073C09E` → [PipDmgReevaluateQueue](PipDmgReevaluateQueue_function_0073C1A4.md) (function, `0x0073C1A4`)
- `0x0073C0A3` → [PnpTraceDmaGuardSystemPolicy](PnpTraceDmaGuardSystemPolicy_function_0073C9C0.md) (function, `0x0073C9C0`)

### Direct callers
- [PiDmaGuardInitialize](../../text/5A/PiDmaGuardInitialize_function_005A9F0C.md) at `0x005A9F43`

### Static image references
- `0x0073C080` → RVA `0x00F8A9AC` (`.data`; read)
- `0x0073C098` → RVA `0x00F8A9AC` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0073C07C  48 83 EC 28                     sub rsp, 0x28
0073C080  83 3D 25 E9 84 00 00            cmp dword ptr [rip + 0x84e925], 0
0073C087  74 1A                           je 0x14073c0a3
0073C089  E8 2A 49 FF FF                  call 0x1407309b8
0073C08E  85 C0                           test eax, eax
0073C090  B9 02 00 00 00                  mov ecx, 2
0073C095  0F 44 C1                        cmove eax, ecx
0073C098  89 05 0E E9 84 00               mov dword ptr [rip + 0x84e90e], eax
0073C09E  E8 01 01 00 00                  call 0x14073c1a4
0073C0A3  E8 18 09 00 00                  call 0x14073c9c0
0073C0A8  33 C0                           xor eax, eax
0073C0AA  48 83 C4 28                     add rsp, 0x28
0073C0AE  C3                              ret
0073C0AF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipDmgInitPhaseTwo(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(v_rip + 8710437)) != 0) {
        result = PipDmgInitReadGroupPolicy(a1, a2, a3, a4);
        a1 = 2;
        if ((unsigned int)(result) == 0) { result = (unsigned int)(a1); }
        *(unsigned int *)(v_rip + 8710414) = (unsigned int)(result);
        result = PipDmgReevaluateQueue(a1, a2, a3, a4);
    }
    result = PnpTraceDmaGuardSystemPolicy(a1, a2, a3, a4);
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PipDmgInitPhaseTwo(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(v_rip + 0x84E925)) != 0) {
        result = PipDmgInitReadGroupPolicy(a1, a2, a3, a4);
        a1 = 2;
        if ((uint32_t)(result) == 0) { result = (uint32_t)(a1); }
        *(uint32_t *)(v_rip + 0x84E90E) = (uint32_t)(result);
        result = PipDmgReevaluateQueue(a1, a2, a3, a4);
    }
    result = PnpTraceDmaGuardSystemPolicy(a1, a2, a3, a4);
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0073C07C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0073C07C[BB_0073C07C]
  bb_0073C089[BB_0073C089]
  bb_0073C0A3[BB_0073C0A3]
  bb_0073C0AF[BB_0073C0AF]
  bb_0073C07C -->|branch| bb_0073C0A3
  bb_0073C07C -->|fallthrough| bb_0073C089
  bb_0073C089 -->|flow| bb_0073C0A3
```
