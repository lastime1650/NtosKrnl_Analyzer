# VfZwAddBootEntry_Entry

- RVA: `0x00BA3CC0`–`0x00BA3CF1` (길이 `49` bytes)
- VA: `0x0000000140BA3CC0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BA3CC9` → [ViZwShouldCheck](ViZwShouldCheck_function_00BA4DB4.md) (function, `0x00BA4DB4`)
- `0x00BA3CD9` → [ViZwCheckVirtualAddress](ViZwCheckVirtualAddress_function_00BA4D68.md) (function, `0x00BA4D68`)
- `0x00BA3CE5` → [ViZwCheckVirtualAddress](ViZwCheckVirtualAddress_function_00BA4D68.md) (function, `0x00BA4D68`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA3CC0  40 53                           push rbx
00BA3CC2  48 83 EC 20                     sub rsp, 0x20
00BA3CC6  48 8B D9                        mov rbx, rcx
00BA3CC9  E8 E6 10 00 00                  call 0x140ba4db4
00BA3CCE  85 C0                           test eax, eax
00BA3CD0  74 18                           je 0x140ba3cea
00BA3CD2  48 8B 13                        mov rdx, qword ptr [rbx]
00BA3CD5  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00BA3CD9  E8 8A 10 00 00                  call 0x140ba4d68
00BA3CDE  48 8B 13                        mov rdx, qword ptr [rbx]
00BA3CE1  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00BA3CE5  E8 7E 10 00 00                  call 0x140ba4d68
00BA3CEA  48 83 C4 20                     add rsp, 0x20
00BA3CEE  5B                              pop rbx
00BA3CEF  C3                              ret
00BA3CF0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfZwAddBootEntry_Entry(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ViZwShouldCheck(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) {
        a2 = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int64 *)(a1 + 16);
        result = ViZwCheckVirtualAddress(a1, a2, a3, a4);
        a2 = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int64 *)(a1 + 8);
        result = ViZwCheckVirtualAddress(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfZwAddBootEntry_Entry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ViZwShouldCheck(Arg1, a2, a3, a4);
    if ((uint32_t)(result) != 0) {
        a2 = *(uint64_t *)(arg1);
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        result = ViZwCheckVirtualAddress(Arg1, a2, a3, a4);
        a2 = *(uint64_t *)(arg1);
        Arg1 = *(uint64_t *)(arg1 + 0x8);
        result = ViZwCheckVirtualAddress(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA3CC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA3CC0[BB_00BA3CC0]
  bb_00BA3CD2[BB_00BA3CD2]
  bb_00BA3CEA[BB_00BA3CEA]
  bb_00BA3CF0[BB_00BA3CF0]
  bb_00BA3CC0 -->|branch| bb_00BA3CEA
  bb_00BA3CC0 -->|fallthrough| bb_00BA3CD2
  bb_00BA3CD2 -->|flow| bb_00BA3CEA
```
