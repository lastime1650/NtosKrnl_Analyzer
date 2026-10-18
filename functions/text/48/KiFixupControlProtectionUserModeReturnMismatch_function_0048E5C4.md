# KiFixupControlProtectionUserModeReturnMismatch

- RVA: `0x0048E5C4`–`0x0048E5E4` (길이 `32` bytes)
- VA: `0x000000014048E5C4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B167C`
- 디코드: `11`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiProcessControlProtection](../44/KiProcessControlProtection_function_00444750.md) at `0x0044499C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0048E5C4  48 8D 51 F8                     lea rdx, [rcx - 8]
0048E5C8  66 4C 0F 38 F5 02               wrussq qword ptr [rdx], r8
0048E5CE  EB 02                           jmp 0x14048e5d2
0048E5D0  EB 10                           jmp 0x14048e5e2
0048E5D2  48 8B C2                        mov rax, rdx
0048E5D5  48 C1 EA 20                     shr rdx, 0x20
0048E5D9  B9 A7 06 00 00                  mov ecx, 0x6a7
0048E5DE  0F 30                           wrmsr
0048E5E0  33 C0                           xor eax, eax
0048E5E2  C3                              ret
0048E5E3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiFixupControlProtectionUserModeReturnMismatch(__int64 a1)
{
    __int64 result;

    goto loc_0048E5D2;
loc_0048E5D2:
    a2 = (a1 - 8) >> (32);
    result = 0;
loc_0048E5E2:
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiFixupControlProtectionUserModeReturnMismatch(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    goto loc_0048E5D2;
loc_0048E5D2:
    a2 = (Arg1 - 8) >> (32);
    result = 0;
loc_0048E5E2:
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x8` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0048E5C4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0048E5C4[BB_0048E5C4]
  bb_0048E5D0[BB_0048E5D0]
  bb_0048E5D2[BB_0048E5D2]
  bb_0048E5E2[BB_0048E5E2]
  bb_0048E5E3[BB_0048E5E3]
  bb_0048E5C4 -->|branch| bb_0048E5D2
  bb_0048E5D0 -->|branch| bb_0048E5E2
  bb_0048E5D2 -->|flow| bb_0048E5E2
```
