# SdbFindNextStringIndexedTag

- RVA: `0x00A914C8`–`0x00A914FF` (길이 `55` bytes)
- VA: `0x0000000140A914C8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `19`개 명령, `55/55` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A914DD` → [SdbpGetNextIndexedRecord](SdbpGetNextIndexedRecord_function_00A91608.md) (function, `0x00A91608`)
- `0x00A914EE` → [SdbpFindMatchingName](SdbpFindMatchingName_function_00A91508.md) (function, `0x00A91508`)

### Direct callers
- [SdbpSearchDB](../AB/SdbpSearchDB_function_00AB3294.md) at `0x00AB353E`
- [SdbpSearchDB](../AB/SdbpSearchDB_function_00AB3294.md) at `0x00AB363C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A914C8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A914CD  57                              push rdi
00A914CE  48 83 EC 20                     sub rsp, 0x20
00A914D2  48 8B DA                        mov rbx, rdx
00A914D5  4C 8B C2                        mov r8, rdx
00A914D8  8B 12                           mov edx, dword ptr [rdx]
00A914DA  48 8B F9                        mov rdi, rcx
00A914DD  E8 26 01 00 00                  call 0x140a91608
00A914E2  85 C0                           test eax, eax
00A914E4  74 0D                           je 0x140a914f3
00A914E6  4C 8B C3                        mov r8, rbx
00A914E9  8B D0                           mov edx, eax
00A914EB  48 8B CF                        mov rcx, rdi
00A914EE  E8 15 00 00 00                  call 0x140a91508
00A914F3  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A914F8  48 83 C4 20                     add rsp, 0x20
00A914FC  5F                              pop rdi
00A914FD  C3                              ret
00A914FE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SdbFindNextStringIndexedTag(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = SdbpGetNextIndexedRecord(a1, (unsigned int)(*(unsigned int *)(a2)), a2, a4);
    if ((unsigned int)(result) != 0) {
        a3 = a2;
        a2 = (unsigned int)(result);
        a1 = a1;
        result = SdbpFindMatchingName(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SdbFindNextStringIndexedTag(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = SdbpGetNextIndexedRecord(Arg1, (uint32_t)(*(uint32_t *)(arg2)), Arg2, a4);
    if ((uint32_t)(result) != 0) {
        a3 = Arg2;
        Arg2 = (uint32_t)(result);
        Arg1 = Arg1;
        result = SdbpFindMatchingName(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A914C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A914C8[BB_00A914C8]
  bb_00A914E6[BB_00A914E6]
  bb_00A914F3[BB_00A914F3]
  bb_00A914FE[BB_00A914FE]
  bb_00A914C8 -->|branch| bb_00A914F3
  bb_00A914C8 -->|fallthrough| bb_00A914E6
  bb_00A914E6 -->|flow| bb_00A914F3
```
