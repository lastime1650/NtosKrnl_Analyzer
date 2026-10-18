# sub_006FB37C

- RVA: `0x006FB37C`–`0x006FB3A7` (길이 `43` bytes)
- VA: `0x00000001406FB37C`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B9328`
- 디코드: `8`개 명령, `43/43` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006FB39D` → [KeCopyXfdMaskToPeb + 0xB](../4B/KeCopyXfdMaskToPeb_function_004B23C4.md) (`tail-transfer`)
  - `0x006FB3A2` → [KeCopyXfdMaskToPeb + 0xB](../4B/KeCopyXfdMaskToPeb_function_004B23C4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006FB37C  48 8B 81 98 01 00 00            mov rax, qword ptr [rcx + 0x198]
006FB383  49 89 80 C8 07 00 00            mov qword ptr [r8 + 0x7c8], rax
006FB38A  48 85 D2                        test rdx, rdx
006FB38D  74 0E                           je 0x1406fb39d
006FB38F  48 8B 81 98 01 00 00            mov rax, qword ptr [rcx + 0x198]
006FB396  48 89 82 80 04 00 00            mov qword ptr [rdx + 0x480], rax
006FB39D  E9 2D 70 DB FF                  jmp 0x1404b23cf
006FB3A2  E9 28 70 DB FF                  jmp 0x1404b23cf
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006FB37C(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    *(unsigned __int64 *)(a3 + 1992) = *(unsigned __int64 *)(a1 + 408);
    result = *(unsigned __int64 *)(a1 + 408);
    if (a2 != 0) {
        result = *(unsigned __int64 *)(a1 + 408);
        *(unsigned __int64 *)(a2 + 1152) = result;
    }
}
```

## 5. (Beta) C Style

```c
int64_t sub_006FB37C(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    *(uint64_t *)(arg3 + 0x7C8) = *(uint64_t *)(arg1 + 0x198);
    result = *(uint64_t *)(arg1 + 0x198);
    if (Arg2 != 0) {
        result = *(uint64_t *)(arg1 + 0x198);
        *(uint64_t *)(Arg2 + 0x480) = result;
    }
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x198` | `64` | `R` |
| `Arg3` | `+ 0x7C8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006FB37C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006FB37C[BB_006FB37C]
  bb_006FB38F[BB_006FB38F]
  bb_006FB39D[BB_006FB39D]
  bb_006FB3A2[BB_006FB3A2]
  bb_006FB37C -->|branch| bb_006FB39D
  bb_006FB37C -->|fallthrough| bb_006FB38F
  bb_006FB38F -->|flow| bb_006FB39D
```
