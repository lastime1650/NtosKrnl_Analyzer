# sub_006E167A

- RVA: `0x006E167A`–`0x006E169E` (길이 `36` bytes)
- VA: `0x00000001406E167A`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000751A4`
- 디코드: `8`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006E167A` → RVA `0x00FC5002` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006E1680` → [MiGetBackgroundHugePageToZero + 0x13B](../31/MiGetBackgroundHugePageToZero_function_0031DD8C.md) (`tail-transfer`)
  - `0x006E1694` → [MiGetBackgroundHugePageToZero + 0x71](../31/MiGetBackgroundHugePageToZero_function_0031DD8C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E167A  3A 15 82 39 8E 00               cmp dl, byte ptr [rip + 0x8e3982]
006E1680  0F 83 41 C8 C3 FF               jae 0x14031dec7
006E1686  0F B6 C2                        movzx eax, dl
006E1689  49 8B 8C C0 A8 3A 00 00         mov rcx, qword ptr [r8 + rax*8 + 0x3aa8]
006E1691  48 85 C9                        test rcx, rcx
006E1694  0F 85 63 C7 C3 FF               jne 0x14031ddfd
006E169A  FE C2                           inc dl
006E169C  EB DC                           jmp 0x1406e167a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E167A(__int64 a1, unsigned __int8 a2, __int64 a3)
{
    a2 = (unsigned __int8)((a2) + 1);
    goto loc_006E167A;
}
```

## 5. (Beta) C Style

```c
int64_t sub_006E167A(int64_t Arg1, uint8_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    Arg2 = (uint8_t)((Arg2) + 1);
    goto loc_006E167A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x3AA8 + rax*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E167A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E167A[BB_006E167A]
  bb_006E1686[BB_006E1686]
  bb_006E169A[BB_006E169A]
  bb_006E167A -->|fallthrough| bb_006E1686
  bb_006E1686 -->|fallthrough| bb_006E169A
  bb_006E169A -->|branch| bb_006E167A
```
