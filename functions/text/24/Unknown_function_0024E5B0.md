# sub_0024E5B0

- RVA: `0x0024E5B0`–`0x0024E5BF` (길이 `15` bytes)
- VA: `0x000000014024E5B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000630CC`
- 디코드: `5`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0024E5B0` → [IovFreeIrpPrivate](../../pagevrfy/BB/IovFreeIrpPrivate_function_00BB6F20.md) (function, `0x00BB6F20`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0024E5B0` → [IovFreeIrpPrivate](../../pagevrfy/BB/IovFreeIrpPrivate_function_00BB6F20.md) (`.text` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0024E5B0  E8 6B 89 96 00                  call 0x140bb6f20
0024E5B5  48 81 C4 80 00 00 00            add rsp, 0x80
0024E5BC  5B                              pop rbx
0024E5BD  C3                              ret
0024E5BE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0024E5B0(void)
{
    __int64 result;
    __int64 v_rsp;

    result = IovFreeIrpPrivate(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
void sub_0024E5B0(void)
{
    int64_t result;
    int64_t local_rsp;

    result = IovFreeIrpPrivate(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (128);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0024E5B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0024E5B0[BB_0024E5B0]
  bb_0024E5BE[BB_0024E5BE]
```
