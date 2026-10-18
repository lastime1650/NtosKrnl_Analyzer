# RtlpCaptureContext2

- RVA: `0x004FE6B0`–`0x004FE6C6` (길이 `22` bytes)
- VA: `0x00000001404FE6B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C24A0`
- 디코드: `11`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlpWalkFrameChain](../2F/RtlpWalkFrameChain_function_002F3ED0.md) at `0x002F405E`
- [RtlRaiseException](../5E/RtlRaiseException_function_005E6B00.md) at `0x005E6BA9`

### Static image references
- `0x004FE6B7` → RVA `0x004FE72F` (`CcSaveNVContext2`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FE6B0  48 51                           push rcx
004FE6B2  9C                              pushfq
004FE6B3  48 83 EC 28                     sub rsp, 0x28
004FE6B7  48 8D 15 71 00 00 00            lea rdx, [rip + 0x71]
004FE6BE  FF E2                           jmp rdx
004FE6C0  CC                              int3
004FE6C1  CC                              int3
004FE6C2  CC                              int3
004FE6C3  CC                              int3
004FE6C4  59                              pop rcx
004FE6C5  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall RtlpCaptureContext2(__int64 a1)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
}
```

## 5. (Beta) C Style

```c
void RtlpCaptureContext2(int64_t Arg1)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FE6B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FE6B0[BB_004FE6B0]
  bb_004FE6C0[BB_004FE6C0]
```
