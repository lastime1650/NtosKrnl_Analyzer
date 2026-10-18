# PopReleaseUserPresentSpinLock

- RVA: `0x004B7A90`–`0x004B7AA8` (길이 `24` bytes)
- VA: `0x00000001404B7A90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004B7A9D` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)

### Direct callers
- [PopSetSystemAwayMode](../../page/75/PopSetSystemAwayMode_function_0075EF00.md) at `0x0075EF62`
- [PopSetSystemAwayMode](../../page/75/PopSetSystemAwayMode_function_0075EF00.md) at `0x0075EF82`

### Static image references
- `0x004B7A96` → RVA `0x00F0DEF8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B7A90  48 83 EC 28                     sub rsp, 0x28
004B7A94  8A D1                           mov dl, cl
004B7A96  48 8D 0D 5B 64 A5 00            lea rcx, [rip + 0xa5645b]
004B7A9D  E8 FE B0 ED FF                  call 0x140392ba0
004B7AA2  48 83 C4 28                     add rsp, 0x28
004B7AA6  C3                              ret
004B7AA7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopReleaseUserPresentSpinLock(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = KeReleaseSpinLock(v_rip + 10839131, a1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopReleaseUserPresentSpinLock(uint8_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = KeReleaseSpinLock(v_rip + 10839131, Arg1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B7A90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B7A90[BB_004B7A90]
  bb_004B7AA7[BB_004B7AA7]
```
