# `SMKM_STORE&lt;SM_TRAITS&gt;::SmStCompareRegionDataCallback&#x27;::`1&#x27;::filt$1

- RVA: `0x006D21DA`–`0x006D2207` (길이 `45` bytes)
- VA: `0x00000001406D21DA`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000789B0`
- 디코드: `13`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D21FA` → [SMKM_STORE<SM_TRAITS>::SmStUnhandledExceptionFilter](../60/SMKM_STORE_SM_TRAITS_SmStUnhandledExceptionFilter_function_0060CC08.md) (function, `0x0060CC08`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006D21DA  40 55                           push rbp
006D21DC  48 83 EC 40                     sub rsp, 0x40
006D21E0  48 8B EA                        mov rbp, rdx
006D21E3  48 89 8D A0 00 00 00            mov qword ptr [rbp + 0xa0], rcx
006D21EA  48 8B D1                        mov rdx, rcx
006D21ED  41 B8 04 00 00 00               mov r8d, 4
006D21F3  48 8B 8D F8 00 00 00            mov rcx, qword ptr [rbp + 0xf8]
006D21FA  E8 09 AA F3 FF                  call 0x14060cc08
006D21FF  90                              nop
006D2200  48 83 C4 40                     add rsp, 0x40
006D2204  5D                              pop rbp
006D2205  C3                              ret
006D2206  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall _SMKM_STORE_SM_TRAITS___SmStCompareRegionDataCallback____1___filt_1(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(a2 + 160) = a1;
    result = SMKM_STORE_SM_TRAITS___SmStUnhandledExceptionFilter(*(unsigned __int64 *)(a2 + 248), a1, 4, a4);
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t _SMKM_STORE_SM_TRAITS___SmStCompareRegionDataCallback____1___filt_1(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(arg2 + 0xA0) = Arg1;
    result = SMKM_STORE_SM_TRAITS___SmStUnhandledExceptionFilter(*(uint64_t *)(arg2 + 0xF8), Arg1, 4, a4);
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0xA0` | `64` | `W` |
| `Arg2` | `+ 0xF8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D21DA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D21DA[BB_006D21DA]
  bb_006D2206[BB_006D2206]
```
