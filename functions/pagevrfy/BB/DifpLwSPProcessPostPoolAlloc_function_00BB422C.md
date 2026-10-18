# DifpLwSPProcessPostPoolAlloc

- RVA: `0x00BB422C`–`0x00BB424E` (길이 `34` bytes)
- VA: `0x0000000140BB422C`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00BB4230` → [ExIsSpecialPoolAddress](../../text/49/ExIsSpecialPoolAddress_function_0049C410.md) (function, `0x0049C410`)

### Direct callers
- [DifpExAllocatePool2_LwSP_Exit](DifpExAllocatePool2_LwSP_Exit_function_00BB41D0.md) at `0x00BB41D8`
- [DifpExFreePoolWithTag_LwSP_Enter](DifpExFreePoolWithTag_LwSP_Enter_function_00BB41F0.md) at `0x00BB41F8`
- [DifpExFreePool_LwSP_Enter](DifpExFreePool_LwSP_Enter_function_00BB4210.md) at `0x00BB4218`

### Static image references
- `0x00BB4239` → RVA `0x00F02468` (`.data`; read/write)
- `0x00BB4241` → RVA `0x00F03EA0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BB4230` → [ExIsSpecialPoolAddress](../../text/49/ExIsSpecialPoolAddress_function_0049C410.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BB422C  48 83 EC 28                     sub rsp, 0x28
00BB4230  E8 DB 81 8E FF                  call 0x14049c410
00BB4235  85 C0                           test eax, eax
00BB4237  74 08                           je 0x140bb4241
00BB4239  F0 48 FF 05 27 E2 34 00         lock inc qword ptr [rip + 0x34e227]
00BB4241  C6 05 58 FC 34 00 00            mov byte ptr [rip + 0x34fc58], 0
00BB4248  48 83 C4 28                     add rsp, 0x28
00BB424C  C3                              ret
00BB424D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifpLwSPProcessPostPoolAlloc(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExIsSpecialPoolAddress(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) {
    }
    *(unsigned __int8 *)(v_rip + 3472472) = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void DifpLwSPProcessPostPoolAlloc(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExIsSpecialPoolAddress(a1, a2, a3, a4);
    if ((uint32_t)(result) != 0) {
    }
    *(uint8_t *)(v_rip + 0x34FC58) = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BB422C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BB422C[BB_00BB422C]
  bb_00BB4239[BB_00BB4239]
  bb_00BB4241[BB_00BB4241]
  bb_00BB424D[BB_00BB424D]
  bb_00BB422C -->|branch| bb_00BB4241
  bb_00BB422C -->|fallthrough| bb_00BB4239
  bb_00BB4239 -->|flow| bb_00BB4241
```
