# PiSwMakePdoInactive

- RVA: `0x0094D9A0`–`0x0094D9B8` (길이 `24` bytes)
- VA: `0x000000014094D9A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PiSwProcessRemove](PiSwProcessRemove_function_0094E3B8.md) at `0x0094E440`
- [PiSwGetChildPdo](../AC/PiSwGetChildPdo_function_00AC3544.md) at `0x00AC3714`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0094D9A0  48 8B 41 40                     mov rax, qword ptr [rcx + 0x40]
0094D9A4  48 8B 10                        mov rdx, qword ptr [rax]
0094D9A7  48 3B 4A 78                     cmp rcx, qword ptr [rdx + 0x78]
0094D9AB  75 05                           jne 0x14094d9b2
0094D9AD  48 83 62 78 00                  and qword ptr [rdx + 0x78], 0
0094D9B2  83 48 08 20                     or dword ptr [rax + 8], 0x20
0094D9B6  C3                              ret
0094D9B7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiSwMakePdoInactive(__int64 a1)
{
    if (a1 == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64)) + 120))) {
    }
    return *(unsigned __int64 *)(a1 + 64);
}
```

## 5. (Beta) C Style

```c
int64_t PiSwMakePdoInactive(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if (Arg1 == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40)) + 0x78))) {
    }
    return *(uint64_t *)(arg1 + 0x40);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0094D9A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0094D9A0[BB_0094D9A0]
  bb_0094D9AD[BB_0094D9AD]
  bb_0094D9B2[BB_0094D9B2]
  bb_0094D9B7[BB_0094D9B7]
  bb_0094D9A0 -->|branch| bb_0094D9B2
  bb_0094D9A0 -->|fallthrough| bb_0094D9AD
  bb_0094D9AD -->|flow| bb_0094D9B2
```
