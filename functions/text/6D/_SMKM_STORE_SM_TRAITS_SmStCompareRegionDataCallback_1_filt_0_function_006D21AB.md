# `SMKM_STORE&lt;SM_TRAITS&gt;::SmStCompareRegionDataCallback&#x27;::`1&#x27;::filt$0

- RVA: `0x006D21AB`–`0x006D21DA` (길이 `47` bytes)
- VA: `0x00000001406D21AB`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000789A4`
- 디코드: `14`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D21CD` → [ST_STORE<SM_TRAITS>::StRegionAccessExceptionFilter](../60/ST_STORE_SM_TRAITS_StRegionAccessExceptionFilter_function_0060E798.md) (function, `0x0060E798`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006D21AB  40 55                           push rbp
006D21AD  48 83 EC 40                     sub rsp, 0x40
006D21B1  48 8B EA                        mov rbp, rdx
006D21B4  48 89 8D 98 00 00 00            mov qword ptr [rbp + 0x98], rcx
006D21BB  48 8B 95 F8 00 00 00            mov rdx, qword ptr [rbp + 0xf8]
006D21C2  48 83 C2 50                     add rdx, 0x50
006D21C6  4C 8D 4D 40                     lea r9, [rbp + 0x40]
006D21CA  45 33 C0                        xor r8d, r8d
006D21CD  E8 C6 C5 F3 FF                  call 0x14060e798
006D21D2  90                              nop
006D21D3  48 83 C4 40                     add rsp, 0x40
006D21D7  5D                              pop rbp
006D21D8  C3                              ret
006D21D9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall _SMKM_STORE_SM_TRAITS___SmStCompareRegionDataCallback____1___filt_0(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(a2 + 152) = a1;
    a2 = (*(unsigned __int64 *)(a2 + 248)) + (80);
    a3 = 0;
    result = ST_STORE_SM_TRAITS___StRegionAccessExceptionFilter(a1, a2, a3, a2 + 64);
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t _SMKM_STORE_SM_TRAITS___SmStCompareRegionDataCallback____1___filt_0(int64_t Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(arg2 + 0x98) = Arg1;
    Arg2 = (*(uint64_t *)(arg2 + 0xF8)) + (80);
    Arg3 = 0;
    result = ST_STORE_SM_TRAITS___StRegionAccessExceptionFilter(Arg1, Arg2, Arg3, Arg2 + 64);
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x40` | `64` | `R` |
| `Arg2` | `+ 0x98` | `64` | `W` |
| `Arg2` | `+ 0xF8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D21AB&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D21AB[BB_006D21AB]
  bb_006D21D9[BB_006D21D9]
```
