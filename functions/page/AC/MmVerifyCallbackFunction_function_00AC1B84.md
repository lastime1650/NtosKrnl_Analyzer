# MmVerifyCallbackFunction

- RVA: `0x00AC1B84`–`0x00AC1B98` (길이 `20` bytes)
- VA: `0x0000000140AC1B84`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AC1B8D` → [MmVerifyCallbackFunctionCheckFlags](../../text/4F/MmVerifyCallbackFunctionCheckFlags_function_004F7360.md) (function, `0x004F7360`)

### Direct callers
- [KeRegisterBoundCallback](../../text/5B/KeRegisterBoundCallback_function_005B1B70.md) at `0x005B1B84`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AC1B8D` → [MmVerifyCallbackFunctionCheckFlags](../../text/4F/MmVerifyCallbackFunctionCheckFlags_function_004F7360.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AC1B84  48 83 EC 28                     sub rsp, 0x28
00AC1B88  BA 20 00 00 00                  mov edx, 0x20
00AC1B8D  E8 CE 57 A3 FF                  call 0x1404f7360
00AC1B92  48 83 C4 28                     add rsp, 0x28
00AC1B96  C3                              ret
00AC1B97  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmVerifyCallbackFunction(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MmVerifyCallbackFunctionCheckFlags(a1, 32, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void MmVerifyCallbackFunction(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MmVerifyCallbackFunctionCheckFlags(a1, 32, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AC1B84&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AC1B84[BB_00AC1B84]
  bb_00AC1B97[BB_00AC1B97]
```
