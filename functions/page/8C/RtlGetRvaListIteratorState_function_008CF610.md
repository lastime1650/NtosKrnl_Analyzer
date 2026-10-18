# RtlGetRvaListIteratorState

- RVA: `0x008CF610`–`0x008CF624` (길이 `20` bytes)
- VA: `0x00000001408CF610`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00084928`
- 디코드: `6`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiImageCfgEnumRvaListFirst](MiImageCfgEnumRvaListFirst_function_008CF598.md) at `0x008CF5DE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008CF622` → [sub_008CF681 + 0x5](Unknown_function_008CF681.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008CF610  48 83 EC 08                     sub rsp, 8
008CF614  44 8B 41 08                     mov r8d, dword ptr [rcx + 8]
008CF618  45 33 DB                        xor r11d, r11d
008CF61B  4C 8B D1                        mov r10, rcx
008CF61E  41 83 F8 01                     cmp r8d, 1
008CF622  76 62                           jbe 0x1408cf686
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall RtlGetRvaListIteratorState(__int64 a1)
{
    __int64 v_r11;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (8);
    v_r11 = 0;
}
```

## 5. (Beta) C Style

```c
void RtlGetRvaListIteratorState(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_r11;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (8);
    local_r11 = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008CF610&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008CF610[BB_008CF610]
```
