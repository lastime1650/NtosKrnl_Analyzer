# SepFreePrimaryGroup

- RVA: `0x0079D180`–`0x0079D1D8` (길이 `88` bytes)
- VA: `0x000000014079D180`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `21`개 명령, `88/88` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0079D1BE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF0A42`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0079D1BE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0079D180  40 53                           push rbx
0079D182  48 83 EC 20                     sub rsp, 0x20
0079D186  48 8B 81 A8 00 00 00            mov rax, qword ptr [rcx + 0xa8]
0079D18D  48 8B D9                        mov rbx, rcx
0079D190  0F B6 50 01                     movzx edx, byte ptr [rax + 1]
0079D194  8D 14 95 08 00 00 00            lea edx, [rdx*4 + 8]
0079D19B  01 91 8C 00 00 00               add dword ptr [rcx + 0x8c], edx
0079D1A1  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
0079D1A8  48 85 D2                        test rdx, rdx
0079D1AB  74 24                           je 0x14079d1d1
0079D1AD  48 8B 89 B0 00 00 00            mov rcx, qword ptr [rcx + 0xb0]
0079D1B4  48 3B CA                        cmp rcx, rdx
0079D1B7  74 18                           je 0x14079d1d1
0079D1B9  44 0F B7 42 02                  movzx r8d, word ptr [rdx + 2]
0079D1BE  E8 7D 96 F2 FF                  call 0x1406c6840
0079D1C3  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
0079D1CA  48 89 83 B8 00 00 00            mov qword ptr [rbx + 0xb8], rax
0079D1D1  48 83 C4 20                     add rsp, 0x20
0079D1D5  5B                              pop rbx
0079D1D6  C3                              ret
0079D1D7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepFreePrimaryGroup(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 184) == 0) goto loc_0079D1D1;
    result = *(unsigned __int64 *)(a1 + 168);
    if ((*(unsigned __int64 *)(a1 + 176)) != (*(unsigned __int64 *)(a1 + 184))) {
        a3 = *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 184) + 2);
        result = memcpy(*(unsigned __int64 *)(a1 + 176), *(unsigned __int64 *)(a1 + 184), a3, a4);
        result = *(unsigned __int64 *)(a1 + 176);
        *(unsigned __int64 *)(a1 + 184) = result;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SepFreePrimaryGroup(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0xB8) == 0) goto loc_0079D1D1;
    result = *(uint64_t *)(arg1 + 0xA8);
    if ((*(uint64_t *)(arg1 + 0xB0)) != (*(uint64_t *)(arg1 + 0xB8))) {
        a3 = *(uint16_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x2);
        result = memcpy(*(uint64_t *)(arg1 + 0xB0), *(uint64_t *)(arg1 + 0xB8), a3, a4);
        result = *(uint64_t *)(arg1 + 0xB0);
        *(uint64_t *)(arg1 + 0xB8) = result;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8C` | `32` | `R/W` |
| `Arg1` | `+ 0xA8` | `64` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0079D180&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0079D180[BB_0079D180]
  bb_0079D1AD[BB_0079D1AD]
  bb_0079D1B9[BB_0079D1B9]
  bb_0079D1D1[BB_0079D1D1]
  bb_0079D1D7[BB_0079D1D7]
  bb_0079D180 -->|branch| bb_0079D1D1
  bb_0079D180 -->|fallthrough| bb_0079D1AD
  bb_0079D1AD -->|branch| bb_0079D1D1
  bb_0079D1AD -->|fallthrough| bb_0079D1B9
  bb_0079D1B9 -->|flow| bb_0079D1D1
```
