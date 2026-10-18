# PspDereferenceSyscallProvider

- RVA: `0x005E22E8`–`0x005E2315` (길이 `45` bytes)
- VA: `0x00000001405E22E8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005E230A` → [PspDestroySyscallProvider](../../page/77/PspDestroySyscallProvider_function_0077E454.md) (function, `0x0077E454`)

### Direct callers
- [PsRegisterSyscallProvider](../../page/77/PsRegisterSyscallProvider_function_0077E140.md) at `0x0077E2B6`
- [PsUnregisterSyscallProvider](../../page/77/PsUnregisterSyscallProvider_function_0077E330.md) at `0x0077E352`
- [PspDetachProcessFromSyscallProvider](../../page/77/PspDetachProcessFromSyscallProvider_function_0077E4BC.md) at `0x0077E504`
- [PspSyscallProviderOptIn](../../page/77/PspSyscallProviderOptIn_function_0077E79C.md) at `0x0077E8EF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x005E230A` → [PspDestroySyscallProvider](../../page/77/PspDestroySyscallProvider_function_0077E454.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E22E8  48 83 EC 28                     sub rsp, 0x28
005E22EC  48 83 C8 FF                     or rax, 0xffffffffffffffff
005E22F0  F0 48 0F C1 41 30               lock xadd qword ptr [rcx + 0x30], rax
005E22F6  48 83 E8 01                     sub rax, 1
005E22FA  7F 13                           jg 0x1405e230f
005E22FC  48 85 C0                        test rax, rax
005E22FF  74 09                           je 0x1405e230a
005E2301  B9 0E 00 00 00                  mov ecx, 0xe
005E2306  CD 29                           int 0x29
005E2308  EB 05                           jmp 0x1405e230f
005E230A  E8 45 C1 19 00                  call 0x14077e454
005E230F  48 83 C4 28                     add rsp, 0x28
005E2313  C3                              ret
005E2314  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspDereferenceSyscallProvider(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (result) | (-1);
    result = (result) - (1);
    if (condition_is_greater) goto loc_005E230F;
    if (result == 0) goto loc_005E230A;
    goto loc_005E230F;
loc_005E230A:
    result = PspDestroySyscallProvider(14, a2, a3, a4);
loc_005E230F:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspDereferenceSyscallProvider(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (result) | (-1);
    result = (result) - (1);
    if (condition_is_greater) goto loc_005E230F;
    if (result == 0) goto loc_005E230A;
    goto loc_005E230F;
loc_005E230A:
    result = PspDestroySyscallProvider(14, a2, a3, a4);
loc_005E230F:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E22E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005E22E8[BB_005E22E8]
  bb_005E22FC[BB_005E22FC]
  bb_005E2301[BB_005E2301]
  bb_005E230A[BB_005E230A]
  bb_005E230F[BB_005E230F]
  bb_005E2314[BB_005E2314]
  bb_005E22E8 -->|branch| bb_005E230F
  bb_005E22E8 -->|fallthrough| bb_005E22FC
  bb_005E22FC -->|branch| bb_005E230A
  bb_005E22FC -->|fallthrough| bb_005E2301
  bb_005E2301 -->|branch| bb_005E230F
  bb_005E230A -->|flow| bb_005E230F
```
