# PspInheritQuota

- RVA: `0x00A6F084`–`0x00A6F0B0` (길이 `44` bytes)
- VA: `0x0000000140A6F084`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PspAllocateProcess](../A1/PspAllocateProcess_function_00A13B3C.md) at `0x00A1511E`
- [PspAllocateProcess](../A1/PspAllocateProcess_function_00A13B3C.md) at `0x00A151C8`

### Static image references
- `0x00A6F0A7` → RVA `0x00E27F80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A6F084  48 85 D2                        test rdx, rdx
00A6F087  74 1E                           je 0x140a6f0a7
00A6F089  48 8B 82 F8 02 00 00            mov rax, qword ptr [rdx + 0x2f8]
00A6F090  F0 FF 80 00 02 00 00            lock inc dword ptr [rax + 0x200]
00A6F097  F0 FF 80 04 02 00 00            lock inc dword ptr [rax + 0x204]
00A6F09E  48 89 81 F8 02 00 00            mov qword ptr [rcx + 0x2f8], rax
00A6F0A5  C3                              ret
00A6F0A6  CC                              int3
00A6F0A7  48 8D 05 D2 8E 3B 00            lea rax, [rip + 0x3b8ed2]
00A6F0AE  EB E0                           jmp 0x140a6f090
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspInheritQuota(__int64 a1, __int64 a2)
{
    if (a2 == 0) goto loc_00A6F0A7;
loc_00A6F090:
    *(unsigned __int64 *)(a1 + 760) = *(unsigned __int64 *)(a2 + 760);
    return *(unsigned __int64 *)(a2 + 760);
loc_00A6F0A7:
    goto loc_00A6F090;
}
```

## 5. (Beta) C Style

```c
int64_t PspInheritQuota(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if (Arg2 == 0) goto loc_00A6F0A7;
loc_00A6F090:
    *(uint64_t *)(arg1 + 0x2F8) = *(uint64_t *)(Arg2 + 0x2F8);
    return *(uint64_t *)(Arg2 + 0x2F8);
loc_00A6F0A7:
    goto loc_00A6F090;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2F8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A6F084&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A6F084[BB_00A6F084]
  bb_00A6F089[BB_00A6F089]
  bb_00A6F090[BB_00A6F090]
  bb_00A6F0A6[BB_00A6F0A6]
  bb_00A6F0A7[BB_00A6F0A7]
  bb_00A6F084 -->|branch| bb_00A6F0A7
  bb_00A6F084 -->|fallthrough| bb_00A6F089
  bb_00A6F089 -->|flow| bb_00A6F090
  bb_00A6F0A6 -->|flow| bb_00A6F0A7
  bb_00A6F0A7 -->|branch| bb_00A6F090
```
