# PiDevCfgConfigureDeviceInterfaceCallback

- RVA: `0x005A7D30`–`0x005A7D62` (길이 `50` bytes)
- VA: `0x00000001405A7D30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `18`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005A7D4D` → [PiDevCfgConfigureDeviceInterface](../../page/96/PiDevCfgConfigureDeviceInterface_function_00963C18.md) (function, `0x00963C18`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x005A7D4D` → [PiDevCfgConfigureDeviceInterface](../../page/96/PiDevCfgConfigureDeviceInterface_function_00963C18.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005A7D30  40 53                           push rbx
005A7D32  48 83 EC 20                     sub rsp, 0x20
005A7D36  41 83 79 10 00                  cmp dword ptr [r9 + 0x10], 0
005A7D3B  49 8B D9                        mov rbx, r9
005A7D3E  48 8B C2                        mov rax, rdx
005A7D41  7C 16                           jl 0x1405a7d59
005A7D43  4D 8B 41 08                     mov r8, qword ptr [r9 + 8]
005A7D47  48 8B C8                        mov rcx, rax
005A7D4A  49 8B 11                        mov rdx, qword ptr [r9]
005A7D4D  E8 C6 BE 3B 00                  call 0x140963c18
005A7D52  85 C0                           test eax, eax
005A7D54  79 03                           jns 0x1405a7d59
005A7D56  89 43 10                        mov dword ptr [rbx + 0x10], eax
005A7D59  32 C0                           xor al, al
005A7D5B  48 83 C4 20                     add rsp, 0x20
005A7D5F  5B                              pop rbx
005A7D60  C3                              ret
005A7D61  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgConfigureDeviceInterfaceCallback(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(a4 + 16)) < 0) goto loc_005A7D59;
    result = PiDevCfgConfigureDeviceInterface(a2, *(unsigned __int64 *)(a4), *(unsigned __int64 *)(a4 + 8), a4);
    if (sign_flag) {
        *(unsigned int *)(a4 + 16) = (unsigned int)(result);
    }
    result = 0;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgConfigureDeviceInterfaceCallback(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(arg4 + 0x10)) < 0) goto loc_005A7D59;
    result = PiDevCfgConfigureDeviceInterface(Arg2, *(uint64_t *)(arg4), *(uint64_t *)(arg4 + 0x8), Arg4);
    if (sign_flag) {
        *(uint32_t *)(arg4 + 0x10) = (uint32_t)(result);
    }
    result = 0;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `32` | `R` |
| `Arg4` | `+ 0x10` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005A7D30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005A7D30[BB_005A7D30]
  bb_005A7D43[BB_005A7D43]
  bb_005A7D56[BB_005A7D56]
  bb_005A7D59[BB_005A7D59]
  bb_005A7D61[BB_005A7D61]
  bb_005A7D30 -->|branch| bb_005A7D59
  bb_005A7D30 -->|fallthrough| bb_005A7D43
  bb_005A7D43 -->|branch| bb_005A7D59
  bb_005A7D43 -->|fallthrough| bb_005A7D56
  bb_005A7D56 -->|flow| bb_005A7D59
```
