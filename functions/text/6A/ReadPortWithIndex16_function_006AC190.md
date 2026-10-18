# ReadPortWithIndex16

- RVA: `0x006AC190`–`0x006AC1B6` (길이 `38` bytes)
- VA: `0x00000001406AC190`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006AC1AB` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006AC1A1` → RVA `0x00E039A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006AC190  48 83 EC 28                     sub rsp, 0x28
006AC194  4C 8B C9                        mov r9, rcx
006AC197  0F B6 C2                        movzx eax, dl
006AC19A  0F B6 49 0E                     movzx ecx, byte ptr [rcx + 0xe]
006AC19E  0F AF C8                        imul ecx, eax
006AC1A1  48 8B 05 F8 77 75 00            mov rax, qword ptr [rip + 0x7577f8]
006AC1A8  49 03 09                        add rcx, qword ptr [r9]
006AC1AB  E8 20 E9 00 00                  call 0x1406baad0
006AC1B0  48 83 C4 28                     add rsp, 0x28
006AC1B4  C3                              ret
006AC1B5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ReadPortWithIndex16(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (unsigned int)((*(unsigned __int8 *)(a1 + 14)) * (a2));
    a1 = (a1) + (*(unsigned __int64 *)(a1));
    result = guard_dispatch_icall(a1, a2, a3, a1);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ReadPortWithIndex16(void *Arg1, uint8_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (uint32_t)((*(uint8_t *)(arg1 + 0xE)) * (Arg2));
    Arg1 = (Arg1) + (*(uint64_t *)(arg1));
    result = guard_dispatch_icall(Arg1, Arg2, a3, Arg1);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0xE` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AC190&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AC190[BB_006AC190]
  bb_006AC1B5[BB_006AC1B5]
```
