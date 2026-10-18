# sub_006FB262

- RVA: `0x006FB262`–`0x006FB274` (길이 `18` bytes)
- VA: `0x00000001406FB262`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B89B8`
- 디코드: `5`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006FB26F` → [PopPepUpdateDripsDeviceVetoMask + 0x7C](../4B/PopPepUpdateDripsDeviceVetoMask_function_004B079C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006FB262  44 09 02                        or dword ptr [rdx], r8d
006FB265  48 8D 52 04                     lea rdx, [rdx + 4]
006FB269  49 83 EA 01                     sub r10, 1
006FB26D  75 F3                           jne 0x1406fb262
006FB26F  E9 A4 55 DB FF                  jmp 0x1404b0818
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_006FB262(__int64 a1, __int64 a2, int a3)
{
    __int64 v_r10;

    v_r10 = (v_r10) - (1);
    if (condition_is_not_equal) goto loc_006FB262;
}
```

## 5. (Beta) C Style

```c
void sub_006FB262(int64_t Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t local_r10;

    local_r10 = (local_r10) - (1);
    if (condition_is_not_equal) goto loc_006FB262;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R/W` |
| `Arg2` | `+ 0x4` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006FB262&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006FB262[BB_006FB262]
  bb_006FB26F[BB_006FB26F]
  bb_006FB262 -->|branch| bb_006FB262
  bb_006FB262 -->|fallthrough| bb_006FB26F
```
