# sub_00342A1A

- RVA: `0x00342A1A`–`0x00342A28` (길이 `14` bytes)
- VA: `0x0000000140342A1A`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000778B4`
- 디코드: `3`개 명령, `14/14` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00342A1E` → [PfSnLogVolumeCreate](../../page/96/PfSnLogVolumeCreate_function_00960AE0.md) (function, `0x00960AE0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00342A1E` → [PfSnLogVolumeCreate](../../page/96/PfSnLogVolumeCreate_function_00960AE0.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00342A23` → [sub_0034228E + 0x18](Unknown_function_0034228E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00342A1A  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00342A1E  E8 BD E0 61 00                  call 0x140960ae0
00342A23  E9 7E F8 FF FF                  jmp 0x1403422a6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00342A1A(__int64 a1)
{
    __int64 result;

    result = PfSnLogVolumeCreate(*(unsigned __int64 *)(a1 + 16), a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00342A1A(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = PfSnLogVolumeCreate(*(uint64_t *)(arg1 + 0x10), a2, a3, a4);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00342A1A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00342A1A[BB_00342A1A]
```
