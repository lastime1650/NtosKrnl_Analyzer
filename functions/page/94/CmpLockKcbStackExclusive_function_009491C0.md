# CmpLockKcbStackExclusive

- RVA: `0x009491C0`–`0x009491FD` (길이 `61` bytes)
- VA: `0x00000001409491C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `20`개 명령, `61/61` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009491DB` → [CmpGetKcbAtLayerHeight](CmpGetKcbAtLayerHeight_function_00949210.md) (function, `0x00949210`)
- `0x009491E3` → [CmpLockKcbExclusive](../86/CmpLockKcbExclusive_function_00861EB0.md) (function, `0x00861EB0`)

### Direct callers
- [CmDeleteLayeredKey](../../text/41/CmDeleteLayeredKey_function_0041B598.md) at `0x0041B67D`
- [sub_006ED542](../../text/6E/Unknown_function_006ED542.md) at `0x006ED5E2`
- [CmpAssignKeySecurity](../7E/CmpAssignKeySecurity_function_007EC8B0.md) at `0x007EC930`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009491C0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
009491C5  57                              push rdi
009491C6  48 83 EC 20                     sub rsp, 0x20
009491CA  33 DB                           xor ebx, ebx
009491CC  48 8B F9                        mov rdi, rcx
009491CF  66 3B 59 02                     cmp bx, word ptr [rcx + 2]
009491D3  7F 1C                           jg 0x1409491f1
009491D5  0F B7 D3                        movzx edx, bx
009491D8  48 8B CF                        mov rcx, rdi
009491DB  E8 30 00 00 00                  call 0x140949210
009491E0  48 8B C8                        mov rcx, rax
009491E3  E8 C8 8C F1 FF                  call 0x140861eb0
009491E8  66 FF C3                        inc bx
009491EB  66 3B 5F 02                     cmp bx, word ptr [rdi + 2]
009491EF  7E E4                           jle 0x1409491d5
009491F1  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
009491F6  48 83 C4 20                     add rsp, 0x20
009491FA  5F                              pop rdi
009491FB  C3                              ret
009491FC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpLockKcbStackExclusive(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    if (0 > (*(unsigned __int16 *)(a1 + 2))) goto loc_009491F1;
loc_009491D5:
    result = CmpGetKcbAtLayerHeight(a1, 0, a3, a4);
    result = CmpLockKcbExclusive(result, 0, a3, a4);
    v_rbx = (unsigned __int16)((v_rbx) + 1);
    if (((unsigned __int16)(v_rbx)) <= (*(unsigned __int16 *)(a1 + 2))) goto loc_009491D5;
loc_009491F1:
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpLockKcbStackExclusive(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    if (0 > (*(uint16_t *)(arg1 + 0x2))) goto loc_009491F1;
loc_009491D5:
    result = CmpGetKcbAtLayerHeight(Arg1, 0, a3, a4);
    result = CmpLockKcbExclusive(result, 0, a3, a4);
    local_rbx = (uint16_t)((local_rbx) + 1);
    if (((uint16_t)(local_rbx)) <= (*(uint16_t *)(arg1 + 0x2))) goto loc_009491D5;
loc_009491F1:
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009491C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009491C0[BB_009491C0]
  bb_009491D5[BB_009491D5]
  bb_009491F1[BB_009491F1]
  bb_009491FC[BB_009491FC]
  bb_009491C0 -->|branch| bb_009491F1
  bb_009491C0 -->|fallthrough| bb_009491D5
  bb_009491D5 -->|branch| bb_009491D5
  bb_009491D5 -->|fallthrough| bb_009491F1
```
