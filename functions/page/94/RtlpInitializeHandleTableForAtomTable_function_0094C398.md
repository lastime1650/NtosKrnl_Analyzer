# RtlpInitializeHandleTableForAtomTable

- RVA: `0x0094C398`–`0x0094C3D2` (길이 `58` bytes)
- VA: `0x000000014094C398`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065BAC`
- 디코드: `21`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0094C3A5` → [ExpAllocateHandleTable](ExpAllocateHandleTable_function_0094C8F0.md) (function, `0x0094C8F0`)

### Direct callers
- [RtlCreateAtomTableEx](../../text/4A/RtlCreateAtomTableEx_function_004A0670.md) at `0x004A06DD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0094C398  40 53                           push rbx
0094C39A  48 83 EC 20                     sub rsp, 0x20
0094C39E  48 8B D9                        mov rbx, rcx
0094C3A1  B2 01                           mov dl, 1
0094C3A3  33 C9                           xor ecx, ecx
0094C3A5  E8 46 05 00 00                  call 0x14094c8f0
0094C3AA  48 8B D0                        mov rdx, rax
0094C3AD  48 85 C0                        test rax, rax
0094C3B0  74 1C                           je 0x14094c3ce
0094C3B2  48 83 C0 18                     add rax, 0x18
0094C3B6  48 89 40 08                     mov qword ptr [rax + 8], rax
0094C3BA  48 89 00                        mov qword ptr [rax], rax
0094C3BD  48 85 D2                        test rdx, rdx
0094C3C0  48 89 53 10                     mov qword ptr [rbx + 0x10], rdx
0094C3C4  0F 95 C0                        setne al
0094C3C7  48 83 C4 20                     add rsp, 0x20
0094C3CB  5B                              pop rbx
0094C3CC  C3                              ret
0094C3CD  CC                              int3
0094C3CE  33 D2                           xor edx, edx
0094C3D0  EB EB                           jmp 0x14094c3bd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpInitializeHandleTableForAtomTable(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = 0;
    result = ExpAllocateHandleTable(a1, 1, a3, a4);
    if (result == 0) goto loc_0094C3CE;
    result = (result) + (24);
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result) = result;
loc_0094C3BD:
    *(unsigned __int64 *)(a1 + 16) = result;
    result = (result != 0) ? 1 : 0;
    v_rsp = (v_rsp) + (32);
    return result;
loc_0094C3CE:
    a2 = 0;
    goto loc_0094C3BD;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpInitializeHandleTableForAtomTable(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = 0;
    result = ExpAllocateHandleTable(Arg1, 1, a3, a4);
    if (result == 0) goto loc_0094C3CE;
    result = (result) + (24);
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result) = result;
loc_0094C3BD:
    *(uint64_t *)(arg1 + 0x10) = result;
    result = (result != 0) ? 1 : 0;
    local_rsp = (local_rsp) + (32);
    return result;
loc_0094C3CE:
    a2 = 0;
    goto loc_0094C3BD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0094C398&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0094C398[BB_0094C398]
  bb_0094C3B2[BB_0094C3B2]
  bb_0094C3BD[BB_0094C3BD]
  bb_0094C3CD[BB_0094C3CD]
  bb_0094C3CE[BB_0094C3CE]
  bb_0094C398 -->|branch| bb_0094C3CE
  bb_0094C398 -->|fallthrough| bb_0094C3B2
  bb_0094C3B2 -->|flow| bb_0094C3BD
  bb_0094C3CD -->|flow| bb_0094C3CE
  bb_0094C3CE -->|branch| bb_0094C3BD
```
