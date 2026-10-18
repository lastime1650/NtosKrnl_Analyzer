# XmPopOp

- RVA: `0x00472560`–`0x0047257F` (길이 `31` bytes)
- VA: `0x0000000140472560`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00472569` → [XmPopStack](XmPopStack_function_00472588.md) (function, `0x00472588`)
- `0x00472573` → [XmStoreResult](XmStoreResult_function_004739FC.md) (function, `0x004739FC`)

### Direct callers
- [XmPopaOp](../57/XmPopaOp_function_00577750.md) at `0x0057779E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00472560  40 53                           push rbx
00472562  48 83 EC 20                     sub rsp, 0x20
00472566  48 8B D9                        mov rbx, rcx
00472569  E8 1A 00 00 00                  call 0x140472588
0047256E  8B D0                           mov edx, eax
00472570  48 8B CB                        mov rcx, rbx
00472573  E8 84 14 00 00                  call 0x1404739fc
00472578  48 83 C4 20                     add rsp, 0x20
0047257C  5B                              pop rbx
0047257D  C3                              ret
0047257E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall XmPopOp(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = XmPopStack(a1, a2, a3, a4);
    result = XmStoreResult(a1, (unsigned int)((unsigned int)(result)), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t XmPopOp(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = XmPopStack(Arg1, a2, a3, a4);
    result = XmStoreResult(Arg1, (uint32_t)((uint32_t)(result)), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00472560&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00472560[BB_00472560]
  bb_0047257E[BB_0047257E]
```
