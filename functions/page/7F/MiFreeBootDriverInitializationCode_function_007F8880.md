# MiFreeBootDriverInitializationCode

- RVA: `0x007F8880`–`0x007F889A` (길이 `26` bytes)
- VA: `0x00000001407F8880`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007F888D` → [MiFreeDriverInitialization](../A4/MiFreeDriverInitialization_function_00A4B120.md) (function, `0x00A4B120`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007F8880  48 83 EC 28                     sub rsp, 0x28
007F8884  F7 41 68 00 00 00 40            test dword ptr [rcx + 0x68], 0x40000000
007F888B  75 05                           jne 0x1407f8892
007F888D  E8 8E 28 25 00                  call 0x140a4b120
007F8892  33 C0                           xor eax, eax
007F8894  48 83 C4 28                     add rsp, 0x28
007F8898  C3                              ret
007F8899  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFreeBootDriverInitializationCode(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((*(unsigned int *)(a1 + 104)) & (0x40000000ULL)) == 0) {
        result = MiFreeDriverInitialization(a1, a2, a3, a4);
    }
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiFreeBootDriverInitializationCode(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((*(uint32_t *)(arg1 + 0x68)) & (0x40000000ULL)) == 0) {
        result = MiFreeDriverInitialization(Arg1, a2, a3, a4);
    }
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x68` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007F8880&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007F8880[BB_007F8880]
  bb_007F888D[BB_007F888D]
  bb_007F8892[BB_007F8892]
  bb_007F8899[BB_007F8899]
  bb_007F8880 -->|branch| bb_007F8892
  bb_007F8880 -->|fallthrough| bb_007F888D
  bb_007F888D -->|flow| bb_007F8892
```
