# RtlpEnvRegisterFaultRange

- RVA: `0x00605864`–`0x00605884` (길이 `32` bytes)
- VA: `0x0000000140605864`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0060586E` → [MmManageFaultRange](../68/MmManageFaultRange_function_00686AD4.md) (function, `0x00686AD4`)

### Direct callers
- [RtlCSparseBitmapStart](RtlCSparseBitmapStart_function_00605338.md) at `0x00605416`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00605864  48 83 EC 28                     sub rsp, 0x28
00605868  41 B9 01 00 00 00               mov r9d, 1
0060586E  E8 61 12 08 00                  call 0x140686ad4
00605873  F7 D8                           neg eax
00605875  1B C0                           sbb eax, eax
00605877  F7 D0                           not eax
00605879  25 9A 00 00 C0                  and eax, 0xc000009a
0060587E  48 83 C4 28                     add rsp, 0x28
00605882  C3                              ret
00605883  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpEnvRegisterFaultRange(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MmManageFaultRange(a1, a2, a3, 1);
    result = (unsigned int)(-(result));
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (0xC000009AULL));
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void RtlpEnvRegisterFaultRange(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MmManageFaultRange(a1, a2, a3, 1);
    result = (uint32_t)(-(result));
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (0xC000009AULL));
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00605864&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00605864[BB_00605864]
  bb_00605883[BB_00605883]
```
