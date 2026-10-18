# KeRundownSecureProcess

- RVA: `0x005B9868`–`0x005B9883` (길이 `27` bytes)
- VA: `0x00000001405B9868`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005B9878` → [VslRundownSecureProcess](../../page/71/VslRundownSecureProcess_function_00719618.md) (function, `0x00719618`)

### Direct callers
- [PspRundownSingleProcess](../../page/90/PspRundownSingleProcess_function_00906D50.md) at `0x00907152`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x005B9878` → [VslRundownSecureProcess](../../page/71/VslRundownSecureProcess_function_00719618.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B9868  48 83 EC 28                     sub rsp, 0x28
005B986C  48 8B 89 70 01 00 00            mov rcx, qword ptr [rcx + 0x170]
005B9873  48 85 C9                        test rcx, rcx
005B9876  74 05                           je 0x1405b987d
005B9878  E8 9B FD 15 00                  call 0x140719618
005B987D  48 83 C4 28                     add rsp, 0x28
005B9881  C3                              ret
005B9882  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeRundownSecureProcess(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(a1 + 368) != 0) {
        result = VslRundownSecureProcess(*(unsigned __int64 *)(a1 + 368), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeRundownSecureProcess(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(arg1 + 0x170) != 0) {
        result = VslRundownSecureProcess(*(uint64_t *)(arg1 + 0x170), a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x170` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B9868&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B9868[BB_005B9868]
  bb_005B9878[BB_005B9878]
  bb_005B987D[BB_005B987D]
  bb_005B9882[BB_005B9882]
  bb_005B9868 -->|branch| bb_005B987D
  bb_005B9868 -->|fallthrough| bb_005B9878
  bb_005B9878 -->|flow| bb_005B987D
```
