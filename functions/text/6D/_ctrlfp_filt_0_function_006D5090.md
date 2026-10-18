# _ctrlfp$filt$0

- RVA: `0x006D5090`–`0x006D50BE` (길이 `46` bytes)
- VA: `0x00000001406D5090`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000BF6EC`
- 디코드: `16`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006D5090  40 55                           push rbp
006D5092  48 83 EC 20                     sub rsp, 0x20
006D5096  48 8B EA                        mov rbp, rdx
006D5099  48 8B 01                        mov rax, qword ptr [rcx]
006D509C  8B 08                           mov ecx, dword ptr [rax]
006D509E  81 F9 05 00 00 C0               cmp ecx, 0xc0000005
006D50A4  74 0C                           je 0x1406d50b2
006D50A6  81 F9 1D 00 00 C0               cmp ecx, 0xc000001d
006D50AC  74 04                           je 0x1406d50b2
006D50AE  33 C0                           xor eax, eax
006D50B0  EB 05                           jmp 0x1406d50b7
006D50B2  B8 01 00 00 00                  mov eax, 1
006D50B7  48 83 C4 20                     add rsp, 0x20
006D50BB  5D                              pop rbp
006D50BC  C3                              ret
006D50BD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall _ctrlfp_filt_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1))))) == 0xC0000005ULL) goto loc_006D50B2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1))))) == 0xC000001DULL) goto loc_006D50B2;
    result = 0;
    goto loc_006D50B7;
loc_006D50B2:
loc_006D50B7:
    v_rsp = (v_rsp) + (32);
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t _ctrlfp_filt_0(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1))))) == 0xC0000005ULL) goto loc_006D50B2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1))))) == 0xC000001DULL) goto loc_006D50B2;
    result = 0;
    goto loc_006D50B7;
loc_006D50B2:
loc_006D50B7:
    local_rsp = (local_rsp) + (32);
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D5090&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D5090[BB_006D5090]
  bb_006D50A6[BB_006D50A6]
  bb_006D50AE[BB_006D50AE]
  bb_006D50B2[BB_006D50B2]
  bb_006D50B7[BB_006D50B7]
  bb_006D50BD[BB_006D50BD]
  bb_006D5090 -->|branch| bb_006D50B2
  bb_006D5090 -->|fallthrough| bb_006D50A6
  bb_006D50A6 -->|branch| bb_006D50B2
  bb_006D50A6 -->|fallthrough| bb_006D50AE
  bb_006D50AE -->|branch| bb_006D50B7
  bb_006D50B2 -->|flow| bb_006D50B7
```
