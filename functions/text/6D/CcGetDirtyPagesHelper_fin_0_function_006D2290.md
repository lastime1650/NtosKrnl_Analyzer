# CcGetDirtyPagesHelper$fin$0

- RVA: `0x006D2290`–`0x006D22BB` (길이 `43` bytes)
- VA: `0x00000001406D2290`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00079818`
- 디코드: `17`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D22AE` → [CcUnpinFileDataEx](../35/CcUnpinFileDataEx_function_00359DEC.md) (function, `0x00359DEC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006D2290  40 55                           push rbp
006D2292  48 83 EC 40                     sub rsp, 0x40
006D2296  48 8B EA                        mov rbp, rdx
006D2299  0F B6 C1                        movzx eax, cl
006D229C  84 C9                           test cl, cl
006D229E  74 14                           je 0x1406d22b4
006D22A0  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
006D22A4  48 85 C9                        test rcx, rcx
006D22A7  74 0B                           je 0x1406d22b4
006D22A9  45 33 C0                        xor r8d, r8d
006D22AC  B2 01                           mov dl, 1
006D22AE  E8 39 7B C8 FF                  call 0x140359dec
006D22B3  90                              nop
006D22B4  48 83 C4 40                     add rsp, 0x40
006D22B8  5D                              pop rbp
006D22B9  C3                              ret
006D22BA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcGetDirtyPagesHelper_fin_0(unsigned __int8 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (64);
    if (a1 == 0) goto loc_006D22B4;
    result = a1;
    if (*(unsigned __int64 *)(a2 + 88) != 0) {
        a3 = 0;
        a2 = 1;
        result = CcUnpinFileDataEx(*(unsigned __int64 *)(a2 + 88), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcGetDirtyPagesHelper_fin_0(uint8_t Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (64);
    if (Arg1 == 0) goto loc_006D22B4;
    result = Arg1;
    if (*(uint64_t *)(arg2 + 0x58) != 0) {
        Arg3 = 0;
        Arg2 = 1;
        result = CcUnpinFileDataEx(*(uint64_t *)(arg2 + 0x58), Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x58` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D2290&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D2290[BB_006D2290]
  bb_006D22A0[BB_006D22A0]
  bb_006D22A9[BB_006D22A9]
  bb_006D22B4[BB_006D22B4]
  bb_006D22BA[BB_006D22BA]
  bb_006D2290 -->|branch| bb_006D22B4
  bb_006D2290 -->|fallthrough| bb_006D22A0
  bb_006D22A0 -->|branch| bb_006D22B4
  bb_006D22A0 -->|fallthrough| bb_006D22A9
  bb_006D22A9 -->|flow| bb_006D22B4
```
