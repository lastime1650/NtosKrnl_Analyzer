# sub_006D8FF8

- RVA: `0x006D8FF8`–`0x006D904B` (길이 `83` bytes)
- VA: `0x00000001406D8FF8`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065110`
- 디코드: `24`개 명령, `83/83` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D900E` → [SMKM_STORE_MGR<SM_TRAITS>::SmCompressCtxCompletePendingEntry](../4A/SMKM_STORE_MGR_SM_TRAITS_SmCompressCtxCompletePendingEntry_function_004A59F8.md) (function, `0x004A59F8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006D9014` → [SMKM_STORE_MGR<SM_TRAITS>::SmCompressCtxProcessEntry + 0x105](../26/SMKM_STORE_MGR_SM_TRAITS_SmCompressCtxProcessEntry_function_002681DC.md) (`tail-transfer`)
  - `0x006D9046` → [SMKM_STORE_MGR<SM_TRAITS>::SmCompressCtxProcessEntry + 0x105](../26/SMKM_STORE_MGR_SM_TRAITS_SmCompressCtxProcessEntry_function_002681DC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006D8FF8  8B 02                           mov eax, dword ptr [rdx]
006D8FFA  4A 8D 0C C5 08 00 00 00         lea rcx, [r8*8 + 8]
006D9002  83 E0 07                        and eax, 7
006D9005  48 0B C8                        or rcx, rax
006D9008  48 89 0A                        mov qword ptr [rdx], rcx
006D900B  48 8B CB                        mov rcx, rbx
006D900E  E8 E5 C9 DC FF                  call 0x1404a59f8
006D9013  90                              nop
006D9014  E9 C8 F2 B8 FF                  jmp 0x1402682e1
006D9019  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
006D901D  48 8B 08                        mov rcx, qword ptr [rax]
006D9020  8B 07                           mov eax, dword ptr [rdi]
006D9022  48 83 E1 F8                     and rcx, 0xfffffffffffffff8
006D9026  83 E0 07                        and eax, 7
006D9029  48 83 C1 08                     add rcx, 8
006D902D  48 0B C8                        or rcx, rax
006D9030  48 89 0F                        mov qword ptr [rdi], rcx
006D9033  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
006D9037  8B 01                           mov eax, dword ptr [rcx]
006D9039  83 E0 07                        and eax, 7
006D903C  48 0B C7                        or rax, rdi
006D903F  48 89 01                        mov qword ptr [rcx], rax
006D9042  48 89 7B 30                     mov qword ptr [rbx + 0x30], rdi
006D9046  E9 96 F2 B8 FF                  jmp 0x1402682e1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006D8FF8(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (7));
    a1 = (a3 * 8 + 8) | (result);
    *(unsigned __int64 *)(a2) = a1;
    result = SMKM_STORE_MGR_SM_TRAITS___SmCompressCtxCompletePendingEntry(v_rbx, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006D8FF8(int64_t Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) & (7));
    Arg1 = (Arg3 * 8 + 8) | (result);
    *(uint64_t *)(arg2) = Arg1;
    result = SMKM_STORE_MGR_SM_TRAITS___SmCompressCtxCompletePendingEntry(local_rbx, Arg2, Arg3, a4);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D8FF8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D8FF8[BB_006D8FF8]
  bb_006D9019[BB_006D9019]
```
