# IoStartTimer

- RVA: `0x00597CF0`–`0x00597D12` (길이 `34` bytes)
- VA: `0x0000000140597CF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00597D07` → [IopEnableTimer](IopEnableTimer_function_00597240.md) (function, `0x00597240`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00597CF0  48 83 EC 28                     sub rsp, 0x28
00597CF4  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00597CFB  8B 50 20                        mov edx, dword ptr [rax + 0x20]
00597CFE  F6 C2 0F                        test dl, 0xf
00597D01  75 09                           jne 0x140597d0c
00597D03  48 8B 49 28                     mov rcx, qword ptr [rcx + 0x28]
00597D07  E8 34 F5 FF FF                  call 0x140597240
00597D0C  48 83 C4 28                     add rsp, 0x28
00597D10  C3                              ret
00597D11  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoStartTimer(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = *(unsigned __int64 *)(a1 + 312);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 32)))) & (15)) == 0) {
        a1 = *(unsigned __int64 *)(a1 + 40);
        result = IopEnableTimer(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 32)), a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IoStartTimer(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = *(uint64_t *)(arg1 + 0x138);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x20)))) & (15)) == 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x28);
        result = IopEnableTimer(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x20)), a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x138` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00597CF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00597CF0[BB_00597CF0]
  bb_00597D03[BB_00597D03]
  bb_00597D0C[BB_00597D0C]
  bb_00597D11[BB_00597D11]
  bb_00597CF0 -->|branch| bb_00597D0C
  bb_00597CF0 -->|fallthrough| bb_00597D03
  bb_00597D03 -->|flow| bb_00597D0C
```
