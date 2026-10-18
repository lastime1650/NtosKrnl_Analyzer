# HalpIommuFlushDomainTB

- RVA: `0x00494C64`–`0x00494C9B` (길이 `55` bytes)
- VA: `0x0000000140494C64`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000789BC`
- 디코드: `15`개 명령, `55/55` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00494C87` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HalpIommuDereferenceHardwareDomain](../55/HalpIommuDereferenceHardwareDomain_function_00554E58.md) at `0x00554ED8`

### Static image references
- `0x00494C68` → RVA `0x00FC1710` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00494C64  48 83 EC 38                     sub rsp, 0x38
00494C68  80 3D A1 CA B2 00 00            cmp byte ptr [rip + 0xb2caa1], 0
00494C6F  75 23                           jne 0x140494c94
00494C71  48 8B 81 88 00 00 00            mov rax, qword ptr [rcx + 0x88]
00494C78  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00494C7C  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00494C81  45 8B C8                        mov r9d, r8d
00494C84  45 33 C0                        xor r8d, r8d
00494C87  E8 44 5E 22 00                  call 0x1406baad0
00494C8C  33 C0                           xor eax, eax
00494C8E  48 83 C4 38                     add rsp, 0x38
00494C92  C3                              ret
00494C93  CC                              int3
00494C94  B8 BB 00 00 C0                  mov eax, 0xc00000bb
00494C99  EB F3                           jmp 0x140494c8e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpIommuFlushDomainTB(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    if ((*(unsigned __int8 *)(v_rip + 11717281)) != 0) goto loc_00494C94;
    v_stack_m18 = a4;
    a3 = 0;
    result = guard_dispatch_icall(*(unsigned __int64 *)(a1 + 16), a2, a3, (unsigned int)(a3));
    result = 0;
loc_00494C8E:
    v_rsp = (v_rsp) + (56);
    return result;
loc_00494C94:
    goto loc_00494C8E;
}
```

## 5. (Beta) C Style

```c
int64_t HalpIommuFlushDomainTB(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    if ((*(uint8_t *)(v_rip + 0xB2CAA1)) != 0) goto loc_00494C94;
    v_stack_m18 = Arg4;
    Arg3 = 0;
    result = guard_dispatch_icall(*(uint64_t *)(arg1 + 0x10), Arg2, Arg3, (uint32_t)(Arg3));
    result = 0;
loc_00494C8E:
    local_rsp = (local_rsp) + (56);
    return result;
loc_00494C94:
    goto loc_00494C8E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x88` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00494C64&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00494C64[BB_00494C64]
  bb_00494C71[BB_00494C71]
  bb_00494C8E[BB_00494C8E]
  bb_00494C93[BB_00494C93]
  bb_00494C94[BB_00494C94]
  bb_00494C64 -->|branch| bb_00494C94
  bb_00494C64 -->|fallthrough| bb_00494C71
  bb_00494C71 -->|flow| bb_00494C8E
  bb_00494C93 -->|flow| bb_00494C94
  bb_00494C94 -->|branch| bb_00494C8E
```
